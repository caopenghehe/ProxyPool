from pyquery import PyQuery as pq

from proxypool.crawlers.base import BaseCrawler
from proxypool.schemas.proxy import Proxy

BASE_URL = 'http://www.xsdaili.cn/dayProxy/ip/3305.html'
BASE_URL2 = 'http://www.xsdaili.cn/dayProxy/ip/3304.html'
headers = {
    'User-Agent': 'Apipost client Runtime/+https://www.apipost.cn/',
}


class XsdailiCrawler(BaseCrawler):
    """
     xsdaili crawler,http://www.xsdaili.cn/dayProxy/ip/3305.html
    """
    urls = [BASE_URL, BASE_URL2]

    def parse(self, html):
        """
        parse html file to get proxies
        :return:
        """
        doc = pq(html)
        items = doc("div.cont").text().split("\n")
        for item in items:
            host = item.split("@")[0].split(":")[0]
            port = item.split("@")[0].split(":")[1]
            yield Proxy(host=host, port=port)


if __name__ == '__main__':
    crawler = XsdailiCrawler()
    for proxy in crawler.crawl():
        print(proxy)
