# from pyquery import PyQuery as pq
#
# from proxypool.crawlers.base import BaseCrawler
# from proxypool.schemas.proxy import Proxy
#
# BASE_URL1 = 'https://www.ip-adress.com/proxy-list'
# headers = {
#     'User-Agent': 'Apipost client Runtime/+https://www.apipost.cn/',
# }
#
# #  ip-adress 代理列表
# class IpAdressCrawler(BaseCrawler):
#     urls = [BASE_URL1]
#
#     def parse(self, html):
#         doc = pq(html)
#         trs = doc('tbody tr').items()
#         for tr in trs:
#             proxs = tr.find('td:nth-child(1)').text().split(":")
#             host = proxs[0]
#             port = int(proxs[1])
#             yield Proxy(host=host, port=port)
#
#
# if __name__ == '__main__':
#     crawler = IpAdressCrawler()
#     for proxy in crawler.crawl():
#         print(proxy)
