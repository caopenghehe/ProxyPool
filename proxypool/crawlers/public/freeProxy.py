# coding=utf-8

from loguru import logger
from pyquery import PyQuery

from proxypool.crawlers.base import BaseCrawler
from proxypool.schemas.proxy import Proxy

BASE_URL = 'https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page={page}'
MAX_PAGE = 100
headers = {
    'User-Agent': 'Apipost client Runtime/+https://www.apipost.cn/',
}


# 反爬 人机校验
# cookie  userno=20210917-006420
#  free proxy lists
class FreeProxyCrawler(BaseCrawler):
    urls = [BASE_URL.format(page=page) for page in range(1, MAX_PAGE + 1)]

    headers = {
        'User-Agent': 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'cookie': 'userno=20210917-006420',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }

    @logger.catch
    def crawl(self):
        for url in self.urls:
            logger.info(f'fetching {url}')
            html = self.fetch(url, headers=self.headers)
            for proxy1 in self.parse(html):
                logger.info(f'fetched proxy {proxy1.string()} from {url}')
                yield proxy1

    def parse(self, html):
        doc = PyQuery(html)
        trs = doc('body > div.layui-main.site-main > div.proxy-table > table > tbody > tr').items()
        for tr in trs:
            if tr.find('td').count() > 2:
                host = tr.find('td:nth-child(0)').text()
                port = int(tr.find('td:nth-child(1)').text())
                yield Proxy(host=host, port=port)


if __name__ == '__main__':
    crawler = FreeProxyCrawler()
    for proxy in crawler.crawl():
        print(proxy)
