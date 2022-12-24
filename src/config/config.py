import os
import json
import datetime
from typing import Literal

_DLSIZE = Literal["square_medium", "medium", "large", "original"]
_SEARCH_TARGET = Literal["partial_match_for_tags", "exact_match_for_tags", "title_and_caption", "keyword", ""]

class Config:
    def __init__(self):
        self.refresh_token = ""
        self.download_path = "./download"
        self.metadata_path = "./metadata"
        self.interval = 1
        self.download_size: _DLSIZE = "medium"
        self.start_date = datetime.date.today()
        self.end_date = datetime.date.today()
        self.search_target: _SEARCH_TARGET = "exact_match_for_tags"

    def load(self, path):
        with(open(path, "r")) as f:
            config = json.load(f)
            self.refresh_token = config["refresh_token"]
            self.download_path = config["download_path"]
            self.metadata_path = config["metadata_path"]
            self.interval = config["interval"]
            self.download_size = config["download_size"]
            self.start_date = datetime.date.fromisoformat(config["start_date"])
            self.end_date = datetime.date.fromisoformat(config["end_date"])
            self.search_target = config["search_target"]

    def save(self, path):
        config = {
            "refresh_token": self.refresh_token,
            "download_path": self.download_path,
            "metadata_path": self.metadata_path,
            "interval": self.interval,
            "download_size": self.download_size,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat(),
            "search_target": self.search_target
        }
        with(open(path, "w")) as f:
            json.dump(config, f, indent=4)

    def input_all(self):
        self.refresh_token = input("Refresh token: ")
        self.download_path = input("Download path: ")
        self.metadata_path = input("Metadata path: ")
        self.interval = int(input("Interval: "))
        self.download_size = input("Download size: ")
        self.start_date = datetime.date.fromisoformat(input("Start date: "))
        self.end_date = datetime.date.fromisoformat(input("End date: "))
        self.search_target = input("Search target: ")

    def input_refresh_token(self):
        self.refresh_token = input("Refresh token: ")

    def __str__(self):
        config = {
            "refresh_token": self.refresh_token,
            "download_path": self.download_path,
            "metadata_path": self.metadata_path,
            "interval": self.interval,
            "download_size": self.download_size,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat(),
            "search_target": self.search_target
        }
        return str(config)