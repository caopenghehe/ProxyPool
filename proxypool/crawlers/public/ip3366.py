import re

from proxypool.crawlers.base import BaseCrawler
from proxypool.schemas.proxy import Proxy

MAX_PAGE = 10
BASE_URL = 'http://www.ip3366.net/free/?stype={stype}&page={page}'
BASE_URL2 = 'https://proxy.ip3366.net/free/?action=china&page={page}'


class IP3366Crawler(BaseCrawler):
    """
    ip3366 crawler, http://www.ip3366.net/
    """
    urls = [(BASE_URL.format(stype=stype, page=i) for stype in range(1, 3) for i in range(1, MAX_PAGE + 1)),
            (BASE_URL2.format(page=i) for i in range(1, MAX_PAGE + 1))]

    def parse(self, html):
        """
        parse html file to get proxies
        :return:
        """
        ip_address = re.compile('<tr>\s*<td>(.*?)</td>\s*<td>(.*?)</td>')
        # \s * 匹配空格，起到换行作用
        re_ip_address = ip_address.findall(html)
        for address, port in re_ip_address:
            yield Proxy(host=address.strip(), port=int(port.strip()))


if __name__ == '__main__':
    crawler = IP3366Crawler()
    for proxy in crawler.crawl():
        print(proxy)
