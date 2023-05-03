# from pyquery import PyQuery as pq
#
# from proxypool.crawlers.base import BaseCrawler
# from proxypool.schemas import Proxy
#
# MAX_PAGE = 10
# BASE_URL = 'http://www.nimadaili.com/{type}/{page}/'
# headers = {
#     'User-Agent': 'Apipost client Runtime/+https://www.apipost.cn/',
# }
#
#
# class NimadailiCrawler(BaseCrawler):
#     """
#     daili66 crawler, http://www.66ip.cn/1.html
#     """
#     urls = [
#         BASE_URL.format(page=page, type=type) for page in range(1, MAX_PAGE + 1) for type in ("gaoni", "http", "https")]
#
#     def parse(self, html):
#         """
#         parse html file to get proxies
#         :return:
#         """
#         doc = pq(html)
#         trs = doc('body > div > div > div > table > tbody > tr').items()
#         for tr in trs:
#             ip = tr.find('td:nth-child(1)').text()
#             host = ip.split(":")[0]
#             port = int(ip.split(":")[1])
#             yield Proxy(host=host, port=port)
#
#
# if __name__ == '__main__':
#     crawler = NimadailiCrawler()
#     for proxy in crawler.crawl():
#         print(proxy)
