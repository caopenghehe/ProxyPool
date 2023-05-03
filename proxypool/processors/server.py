from flask import Flask, g

from proxypool.setting import API_HOST, API_PORT, API_THREADED, IS_DEV
from proxypool.storages.redis import RedisClient

__all__ = ['app']

app = Flask(__name__)
if IS_DEV:
    app.debug = True


def get_conn():
    """
    get redis client object
    :return:
    """
    if not hasattr(g, 'redis'):
        g.redis = RedisClient()
    return g.redis


@app.route('/')
def index():
    """
    get home page, you can define your own templates
    :return:
    """
    conn = get_conn()

    return '<h2>Welcome to Proxy Pool System</h2>' \
           '<h2>当前代理ip数量 ' + str(conn.count()) + \
           '</h2><h3><a href="/random">随机一个代理</a> </h3>' \
           '<h3><a href="/all">显示全部代理</a> </h3>' \
           '<h3><a href="/count">代理ip数量</a> </h3>'


@app.route('/random')
def get_proxy():
    """
    get a random proxy
    :return: get a random proxy
    """
    conn = get_conn()
    return conn.random().string()


@app.route('/all')
def get_proxy_all():
    """
    get a random proxy
    :return: get a random proxy
    """
    conn = get_conn()
    proxies = conn.all()
    proxies_string = ''
    if proxies:
        for proxy in proxies:
            proxies_string += str(proxy) + '\n'

    return proxies_string


@app.route('/count')
def get_count():
    """
    get the count of proxies
    :return: count, int
    """
    conn = get_conn()
    return str(conn.count())


if __name__ == '__main__':
    app.run(host=API_HOST, port=API_PORT, threaded=API_THREADED)
