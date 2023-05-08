from pyquery import PyQuery as pq

from proxypool.crawlers.base import BaseCrawler
from proxypool.schemas.proxy import Proxy

BASE_URL = 'https://dev.kdlapi.com/api/getproxy/?secret_id=o6louq16eyxx9i6vdg5s&num=100&protocol=1&method=1&quality=1&signature=j1h4vvtmtmanduc2szb1aurmateosuaq&sep=4'

headers = {
    'User-Agent': 'Apipost client Runtime/+https://www.apipost.cn/',
}


#  Kuaidailiopen 代理列表
class Kuaidailiopen(BaseCrawler):
    urls = [BASE_URL]

    def parse(self, html):
        doc = pq(html)
        lists = doc.text().split("|")
        for item in lists:
            text = item.split(":")
            if len(text) == 2:
                host = text[0]
                port = int(text[1])
                yield Proxy(host=host, port=port)


if __name__ == '__main__':
    crawler = Kuaidailiopen()
    for proxy in crawler.crawl():
        print(proxy)
