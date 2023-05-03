from pyquery import PyQuery as pq

from proxypool.crawlers.base import BaseCrawler
from proxypool.schemas.proxy import Proxy

BASE_URL = 'https://www.marcosbl.com/lab/proxies/'
MAX_PAGE = 10
headers = {
    'User-Agent': 'Apipost client Runtime/+https://www.apipost.cn/',
}


#  MarcosBL 代理列表
class KxdailiCrawler(BaseCrawler):
    """
     MarcosBL crawler,https://www.marcosbl.com/lab/proxies/
    """
    urls = [BASE_URL]

    def parse(self, html):
        """
        parse html file to get proxies
        :return:
        """
        doc = pq(html)
        trs = doc('#datable tbody tr:gt(0)').items()
        for tr in trs:
            text = tr.find('td:nth-child(2)').text()
            host = text.split(":")[0]
            port = int(text.split(":")[1])
            yield Proxy(host=host, port=port)


if __name__ == '__main__':
    crawler = KxdailiCrawler()
    for proxy in crawler.crawl():
        print(proxy)
