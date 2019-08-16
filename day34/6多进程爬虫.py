# coding:utf-8
import requests
import time
from bs4 import BeautifulSoup


def task(url):

    r1 = requests.get(
        url=url,
        headers={
            'User-Agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/75.0.3770.142 Safari/537.36'
        }
    )

    soup = BeautifulSoup(r1.text, 'html.parser')
    print(soup)


task(url='http://dig.chouti.com/all/hot/recent/01')