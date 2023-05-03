from pyquery import PyQuery as pq

from proxypool.crawlers.base import BaseCrawler
from proxypool.schemas.proxy import Proxy

BASE_URL1 = 'http://pubproxy.com/api/proxy?limit=20&format=txt'
headers = {
    'User-Agent': 'Apipost client Runtime/+https://www.apipost.cn/',
}


#  pubproxy 代理列表
class PubproxyCrawler(BaseCrawler):
    urls = [BASE_URL1]

    def parse(self, html):
        doc = pq(html)
        lists = doc.text().split(" ")
        for item in lists:
            text = item.split(":")
            if len(text) == 2:
                host = text[0]
                port = int(text[1])
                yield Proxy(host=host, port=port)


if __name__ == '__main__':
    crawler = PubproxyCrawler()
    for proxy in crawler.crawl():
        print(proxy)
