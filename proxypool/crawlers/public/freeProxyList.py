from pyquery import PyQuery

from proxypool.crawlers.base import BaseCrawler
from proxypool.schemas.proxy import Proxy

BASE_URL = 'https://free-proxy-list.net/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
}


class FreeProxyList(BaseCrawler):
    """
    free-proxy-list crawler, https://free-proxy-list.net/
    """
    urls = [BASE_URL]

    def parse(self, html):
        """
        parse html file to get proxies
        :return:
        """
        doc = PyQuery(html)
        trs = doc('table.table tbody tr:eq(0)').items()
        for tr in trs:
            host = tr.find('td:nth-child(1)').text()
            port = int(tr.find('td:nth-child(2)').text())
            yield Proxy(host=host, port=port)


if __name__ == '__main__':
    crawler = FreeProxyList()
    for proxy in crawler.crawl():
        print(proxy)
