# pixiv-scraper
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](http://colab.research.google.com/github/yunkai1841/pixiv-scraper/blob/main/notebook/pixiv_scraper.ipynb)
![MIT license](https://img.shields.io/github/license/yunkai1841/pixiv-scraper)

Download images from pixiv.net

## Requirements
- python3
- pixivpy3=latest
- cloudscraper=latest

**Note**: be sure to use the **latest** cloudscraper.

## Usage
1. install requirements
2. get your pixiv refresh token
3. run `python pixiv_scraper.py` (or you can use jupyter notebook)
4. enjoy!

**Note**: you can edit `config.json` to change search condition.

## How to get refresh token
> To get `refresh_token`, see [@ZipFile Pixiv OAuth Flow](https://gist.github.com/ZipFile/c9ebedb224406f4f11845ab700124362) or [OAuth with Selenium/ChromeDriver]( https://gist.github.com/upbit/6edda27cb1644e94183291109b8a5fde)

[Read pixivpy](https://github.com/upbit/pixivpy/blob/7b20c3bd158d10238d27135309525946d39bdbe4/README.md?plain=1#L6)

## parameters
See `pixiv_scraper.py` for more details.