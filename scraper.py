import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            # "htm"を含むURLがないみたいで
            # 本文のとおり↓では何も表示されなかった
            # if url is None:
            #    continue
            # if "html" in url:
            #    prrint("\n" + url)
            # 仕方がないので、hrefタグを全部出してみる
            print(url)
            # thanks! https://teratail.com/questions/150749
            # ちなみに日経BP社から2018年10月16日付で補足↓も出ているが
            # https://shop.nikkeibp.co.jp/front/commodity/0000/C92270/
            # こちらも構造が変更になっているようで、うまくいかなかった

news = "https://news.google.com/"
Scraper(news).scrape()
