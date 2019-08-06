# coding:utf-8
import threading
import requests
import uuid

url_list = []


def task(url):
    ret = requests.get(url)
    file_name = str(uuid.uuid4())+'.jpg'
    with open(file_name, mode='wb')as f:
        f.write(ret.content)


for url in url_list:
    t = threading.Thread(target=task, args=(url,))
