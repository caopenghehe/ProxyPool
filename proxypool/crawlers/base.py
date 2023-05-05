import time

import requests
from fake_headers import Headers
from loguru import logger
from retrying import RetryError, retry

from proxypool.setting import GET_TIMEOUT


class BaseCrawler(object):
    urls = []

    @retry(stop_max_attempt_number=3, retry_on_result=lambda x: x is None, wait_fixed=2000)
    def fetch(self, url, **kwargs):
        try:
            headers = Headers(headers=True).generate()
            kwargs.setdefault('timeout', GET_TIMEOUT)
            kwargs.setdefault('verify', False)
            kwargs.setdefault('headers', headers)
            proxy = requests.get("http://127.0.0.1:5555/random").text.strip()
            proxies = {
                "http": "http://" + proxy,
                "https": "https://" + proxy,
            }
            kwargs.setdefault("proxies", proxies)
            response = requests.get(url, **kwargs)
            if response.status_code == 200:
                response.encoding = 'utf-8'
                return response.text
        except (requests.ConnectionError, requests.ReadTimeout):
            return

    def process(self, html, url):
        """
        used for parse html
        """
        for proxy in self.parse(html):
            logger.info(f'fetched proxy {proxy.string()} from {url}')
            yield proxy

    def crawl(self):
        """
        crawl main method
        """
        try:
            for url in self.urls:
                logger.info(f'fetching {url}')
                html = self.fetch(url)
                if not html:
                    continue
                time.sleep(.5)
                yield from self.process(html, url)
        except RetryError:
            logger.error(
                f'crawler {self} crawled proxy unsuccessfully, '
                'please check if target url is valid or network issue')
