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
            if url is None:
               continue
            if "html" in url:
               print("\n" + url)
            # 上記がうまくいかないときに、hrefタグを全部出してみる版↓
            # print(url)
            # thanks! https://teratail.com/questions/150749
            
            # ちなみに日経BP社から2018年10月16日付で補足↓も出ているが
            # https://shop.nikkeibp.co.jp/front/commodity/0000/C92270/
            # こちらも構造が変更になっているようで、うまくいかなかった

# google news のサイトでは
# "html"を含むURLがないみたいで
# 本文のとおり↓では何も表示されなかった 
# news = "https://news.google.com/"
news = "https://www.yahoo.com/"
# 原著者のGitHubページでは、↑のようにサイトを変更するのが簡単、ということになってる様子
# https://github.com/calthoff/self_taught/issues/21#issuecomment-457426380
Scraper(news).scrape()
