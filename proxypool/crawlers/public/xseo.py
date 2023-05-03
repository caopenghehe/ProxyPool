from pyquery import PyQuery as pq

from proxypool.crawlers.base import BaseCrawler
from proxypool.schemas.proxy import Proxy

BASE_URL2 = 'https://xseo.in/freeproxy'
headers = {
    'User-Agent': 'Apipost client Runtime/+https://www.apipost.cn/',
}


#  Xseo 代理列表
class XseoCrawler(BaseCrawler):
    urls = [BASE_URL2]

    def parse(self, html):
        doc = pq(html)
        trs = doc('.cls8').items()
        for tr in trs:
            text = tr.find('td:nth-child(1)').text().split(":")
            if len(text) == 2:
                host = text[0]
                port = int(text[1])
                yield Proxy(host=host, port=port)
        trs = doc('.cls81').items()
        for tr in trs:
            text = tr.find('td:nth-child(1)').text().split(":")
            if len(text) == 2:
                host = text[0]
                port = int(text[1])
                yield Proxy(host=host, port=port)


if __name__ == '__main__':
    crawler = XseoCrawler()
    for proxy in crawler.crawl():
        print(proxy)
