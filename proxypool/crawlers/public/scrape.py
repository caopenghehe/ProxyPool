from pyquery import PyQuery as pq

from proxypool.crawlers.base import BaseCrawler
from proxypool.schemas.proxy import Proxy

BASE_URL = 'https://proxypool.scrape.center/all'


class ScrapeCrawler(BaseCrawler):
    """
    本项目示例网站代理列表 crawler, https://proxypool.scrape.center/all
    """
    urls = [BASE_URL]

    def parse(self, html):
        """
        parse html file to get proxies
        :return:
        """
        doc = pq(html)
        lists = doc.text().split(" ")
        for item in lists:
            text = item.split(":")
            if len(text) == 2:
                host = text[0]
                port = int(text[1])
                yield Proxy(host=host, port=port)


if __name__ == '__main__':
    crawler = ScrapeCrawler()
    for proxy in crawler.crawl():
        print(proxy)
