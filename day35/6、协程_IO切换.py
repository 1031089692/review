# coding:utf-8
from gevent import monkey
monkey.patch_all()  # 下面代码中遇到IO都会自动执行greenlet的switch进行切换
import requests
import gevent

def get_page_1(url):
    ret = requests.get(url)
    print(url, ret.content)


def get_page_2(url):
    ret = requests.get(url)
    print(url, ret.content)


def get_page_3(url):
    ret = requests.get(url)
    print(url, ret.content)

gevent.joinall([
    gevent.spawn(get_page_1, 'https://www.python.org/'),  # 协程1
    gevent.spawn(get_page_2, 'https://www.yahoo.com/'),  # 协程2
    gevent.spawn(get_page_3, 'https://www.github.com/'),  # 协程3
])
