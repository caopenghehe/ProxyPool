from proxypool.crawlers.base import BaseCrawler
from proxypool.schemas.proxy import Proxy

BASE_URL1 = 'https://www.proxy-list.download/api/v1/get?type=http'
BASE_URL2 = 'https://www.proxy-list.download/api/v1/get?type=https'
BASE_URL3 = 'https://www.proxy-list.download/api/v1/get?type=socks4'
BASE_URL4 = 'https://www.proxy-list.download/api/v1/get?type=socks5'

headers = {
    'User-Agent': 'Apipost client Runtime/+https://www.apipost.cn/',
}


#  proxy-list 代理列表
class ProxyListCrawler(BaseCrawler):
    urls = [BASE_URL1, BASE_URL2, BASE_URL3, BASE_URL4]

    def parse(self, html):
        lists = html.split("\r\n")
        for item in lists:
            text = item.split(":")
            if len(text) == 2:
                host = text[0]
                port = int(text[1])
                yield Proxy(host=host, port=port)


if __name__ == '__main__':
    crawler = ProxyListCrawler()
    for proxy in crawler.crawl():
        print(proxy)
