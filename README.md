# pixiv-scraper
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](http://colab.research.google.com/github/yunkai1841/pixiv-scraper/blob/main/notebook/pixiv_scraper.ipynb)

Download images from pixiv.net

## requirements
- python>=3.6
- pixivpy3=latest
- cloudscraper=latest

**Note**: be sure to use the **latest** cloudscraper.

## usage
1. install requirements
2. get your pixiv refresh token
3. rename `config.py.example` to `config.py` and fill in your `refresh_token`
4. change parameters in `pixiv_scraper.py`
5. run `python pixiv_scraper.py` (or you can use jupyter notebook)

## refresh token
> To get `refresh_token`, see [@ZipFile Pixiv OAuth Flow](https://gist.github.com/ZipFile/c9ebedb224406f4f11845ab700124362) or [OAuth with Selenium/ChromeDriver]( https://gist.github.com/upbit/6edda27cb1644e94183291109b8a5fde)

[Read pixivpy](https://github.com/upbit/pixivpy/blob/7b20c3bd158d10238d27135309525946d39bdbe4/README.md?plain=1#L6)

## parameters
See `pixiv_scraper.py` for more details.