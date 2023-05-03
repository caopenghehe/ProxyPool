# from pyquery import PyQuery as pq
#
# from proxypool.crawlers.base import BaseCrawler
# from proxypool.schemas.proxy import Proxy
#
# BASE_URL1 = 'http://api.foxtools.ru/v2/Proxy.txt'
# BASE_URL2 = 'http://api.foxtools.ru/v2/Proxy.txt?page=%25d'
#
# headers = {
#     'User-Agent': 'Apipost client Runtime/+https://www.apipost.cn/',
# }
# #  FoxTools 代理列表
# class FoxToolsCrawler(BaseCrawler):
#     urls = [BASE_URL1, BASE_URL2]
#
#     def parse(self, html):
#         doc = pq(html)
#         lists = doc.text().split(" ")
#         for item in lists:
#             text = item.split(":")
#             if len(text) == 2:
#                 host = text[0]
#                 port = int(text[1])
#                 yield Proxy(host=host, port=port)
#
#
# if __name__ == '__main__':
#     crawler = FoxToolsCrawler()
#     for proxy in crawler.crawl():
#         print(proxy)
