from pyquery import PyQuery as pq

from proxypool.crawlers.base import BaseCrawler
from proxypool.schemas.proxy import Proxy

BASE_URL = 'https://freeproxylist.ru/proxy-list?page={page}'
MAX_PAGE = 5


class Freeproxylistru(BaseCrawler):
    """
    Freeproxylistru crawler, https://freeproxylist.ru/
    """

    urls = ["https://freeproxylist.ru/", ]
    urls += [BASE_URL.format(page=page) for page in range(2, MAX_PAGE + 1)]

    def parse(self, html):
        """
        parse html file to get proxies
        :return:
        """
        doc = pq(html)
        trs = doc('tbody.table-proxy-list > tr').items()
        for tr in trs:
            host = tr.find('th:nth-child(1)').text()
            port = int(tr.find('td:nth-child(2)').text())
            yield Proxy(host=host, port=port)


if __name__ == '__main__':
    crawler = Freeproxylistru()
    for proxy in crawler.crawl():
        print(proxy)
