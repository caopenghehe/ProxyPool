import requests
from fake_headers import Headers
from pyquery import PyQuery as pq
from retrying import retry

from proxypool.crawlers.base import BaseCrawler
from proxypool.schemas.proxy import Proxy
from proxypool.setting import GET_TIMEOUT

BASE_URL1 = 'https://list.proxylistplus.com/Fresh-HTTP-Proxy-List-{page}'
MAX_PAGE = 6
headers = {
    'User-Agent': 'Apipost client Runtime/+https://www.apipost.cn/',
}


# 编码不稳定?
#  ipaddress 代理列表
class ProxyListPlusCrawler(BaseCrawler):
    urls = [BASE_URL1.format(page=i) for i in range(1, MAX_PAGE + 1)]

    @retry(stop_max_attempt_number=3, retry_on_result=lambda x: x is None, wait_fixed=2000)
    def fetch(self, url, **kwargs):
        proxy = requests.get("http://127.0.0.1:5555/random").text.strip()
        proxies = {
            "http": "http://" + proxy,
            "https": "https://" + proxy,
        }
        kwargs.setdefault("proxies", proxies)
        headers = Headers(headers=True).generate()
        kwargs.setdefault('timeout', GET_TIMEOUT)
        kwargs.setdefault('verify', False)
        kwargs.setdefault('headers', headers)
        try:
            response = requests.get(url, **kwargs)
            if response.status_code == 200:
                response.encoding = 'GBK'
                return response.text
        except requests.ConnectionError:
            return None

    def parse(self, html):
        doc = pq(html)
        trs = doc('table.bg tr:eq(2)').items()
        for tr in trs:
            host = tr.find('td:nth-child(2)').text()
            port = int(tr.find('td:nth-child(3)').text())
            yield Proxy(host=host, port=port)


if __name__ == '__main__':
    crawler = ProxyListPlusCrawler()
    for proxy in crawler.crawl():
        print(proxy)
