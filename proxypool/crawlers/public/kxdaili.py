from pyquery import PyQuery

from proxypool.crawlers.base import BaseCrawler
from proxypool.schemas.proxy import Proxy

BASE_URL = 'http://www.kxdaili.com/dailiip/{types}/{page}.html'
MAX_PAGE = 10
headers = {
    'User-Agent': 'Apipost client Runtime/+https://www.apipost.cn/',
}


#  开心代理
class KxdailiCrawler(BaseCrawler):
    """
     kxdaili crawler, http://www.kxdaili.com/dailiip/1/1.html
    """
    urls = [BASE_URL.format(types=types, page=page) for types in range(1, 3) for page in range(1, MAX_PAGE + 1)]

    def parse(self, html):
        """
        parse html file to get proxies
        :return:
        """
        doc = PyQuery(html)
        trs = doc('table.active tbody tr:eq(0)').items()
        for tr in trs:
            host = tr.find('td:nth-child(1)').text()
            port = int(tr.find('td:nth-child(2)').text())
            yield Proxy(host=host, port=port)


if __name__ == '__main__':
    crawler = KxdailiCrawler()
    for proxy in crawler.crawl():
        print(proxy)
