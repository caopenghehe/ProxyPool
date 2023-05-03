from proxypool.crawlers.base import BaseCrawler
from proxypool.schemas.proxy import Proxy

BASE_URL = 'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt'

headers = {
    'User-Agent': 'Apipost client Runtime/+https://www.apipost.cn/',
}


class Githubusercontent(BaseCrawler):
    """
    Githubusercontent crawler, https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt
    """
    urls = [BASE_URL]

    def parse(self, html):
        """
        parse html file to get proxies
        :return:
        """
        re_ip_address = str(html).split("\n")
        for ip in re_ip_address:
            if ip.strip() != '':
                address, port = ip.split(":")
                yield Proxy(host=address.strip(), port=int(port.strip()))


if __name__ == '__main__':
    crawler = Githubusercontent()
    for proxy in crawler.crawl():
        print(proxy)
