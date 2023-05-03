import datetime
import json

from proxypool.crawlers.base import BaseCrawler
from proxypool.schemas.proxy import Proxy

BASE_URL = 'https://checkerproxy.net/api/archive/{date}'
today = date = datetime.date.today()
headers = {
    'User-Agent': 'Apipost client Runtime/+https://www.apipost.cn/',
}


#  checkerproxy 代理列表
class CheckerproxyCrawler(BaseCrawler):
    urls = [BASE_URL.format(date=today),
            BASE_URL.format(date=today - datetime.timedelta(days=1)),
            BASE_URL.format(date=today - datetime.timedelta(days=2)),
            BASE_URL.format(date=today - datetime.timedelta(days=3))
            ]

    def parse(self, html):
        for item in json.loads(html):
            text = item.get('addr').split(":")
            if len(text) == 2:
                host = text[0]
                port = int(text[1])
                yield Proxy(host=host, port=port)


if __name__ == '__main__':
    crawler = CheckerproxyCrawler()
    for proxy in crawler.crawl():
        print(proxy)
