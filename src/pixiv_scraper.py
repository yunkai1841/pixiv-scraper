from pixivpy3 import AppPixivAPI
from time import sleep
import os
import datetime
import json

from config.config import Config

# Parameters
config = Config()
if os.path.exists("config.json"):
    config.load("config.json")
else:
    # config.input_all()
    config.input_refresh_token()
    config.save("config.json")

TOKEN = config.refresh_token
DL_PATH = config.download_path
METADATA_PATH = config.metadata_path
INTERVAL = config.interval
DL_SIZE = config.download_size
START_DATE = config.start_date
END_DATE = config.end_date
SEARCH_TARGET = config.search_target

search_word = input("Search word: ")

# Login
api = AppPixivAPI()
api.auth(refresh_token=TOKEN)

# Download
if not os.path.exists(DL_PATH):
    os.makedirs(DL_PATH)
if not os.path.exists(METADATA_PATH):
    os.makedirs(METADATA_PATH)

for d in range((END_DATE - START_DATE).days + 1):
    date = START_DATE + datetime.timedelta(days=d)
    date_str = date.strftime("%Y-%m-%d")
    print("Downloading images in %s" % date_str)
    json_result = api.search_illust(search_word, start_date=date_str, end_date=date_str, search_target=SEARCH_TARGET)
    if not json_result.illusts:
        print("No images found in %s" % date_str)
        sleep(INTERVAL)
        continue
    date_dl_path = DL_PATH + "/" + date_str
    if not os.path.exists(date_dl_path):
        os.makedirs(date_dl_path)

    while True:
        for illust in json_result.illusts:
            print("[%s] %s" % (illust.title, illust.image_urls[DL_SIZE]))
            api.download(illust.image_urls[DL_SIZE], path=date_dl_path)
            with open(METADATA_PATH + "/" + date_str + ".txt", "a", encoding="utf-8") as f:
                f.write(str(illust) + "\n")
            sleep(INTERVAL)
        next_qs = api.parse_qs(json_result.next_url)
        with open(METADATA_PATH + "/next_qs.txt", "a", encoding="utf-8") as f:
            f.write(str(next_qs) + "\n")
            f.write(str(json_result.next_url) + "\n")
        if next_qs:
            json_result = api.search_illust(**next_qs)

            # Retry
            # *Note: authentification is required for every 3600 seconds
            for _ in range(10):
                if json_result.illusts:
                    break
                try:
                    api.auth(refresh_token=TOKEN)
                    json_result = api.search_illust(**next_qs)
                    sleep(INTERVAL*10)
                except:
                    pass
            if not json_result.illusts:
                with open(METADATA_PATH + "/error.txt", "a", encoding="utf-8") as f:
                    f.write(str(next_qs) + "\n")
                    f.write(str(json_result) + "\n")
                break
        else:
            break
        sleep(INTERVAL)