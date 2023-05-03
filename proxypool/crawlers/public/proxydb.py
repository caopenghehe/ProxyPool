from pyquery import PyQuery as pq

from proxypool.crawlers.base import BaseCrawler
from proxypool.schemas.proxy import Proxy

BASE_URL1 = 'http://proxydb.net/?protocol=http&protocol=https&country='
headers = {
    'User-Agent': 'Apipost client Runtime/+https://www.apipost.cn/',
}


#  proxydb 代理列表
class ProxydbCrawler(BaseCrawler):
    urls = [BASE_URL1]

    def parse(self, html):
        doc = pq(html)
        trs = doc('tbody tr').items()
        for tr in trs:
            proxs = tr.find('td:nth-child(1)').text().split(":")
            host = proxs[0]
            port = int(proxs[1])
            yield Proxy(host=host, port=port)


if __name__ == '__main__':
    crawler = ProxydbCrawler()
    for proxy in crawler.crawl():
        print(proxy)
