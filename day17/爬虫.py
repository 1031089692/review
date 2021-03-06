# coding:utf-8
import re
from urllib.request import urlopen


def getPage(url):  # 获取整个html的字符串
    response = urlopen(url)
    return response.read().decode('utf-8')


def parsePage(s):
    ret = com.finditer(s)  # 从这个html中，找到所有符合com正则表达式规则的内容并且以迭代器的形式返回
    for i in ret:
        yield {
            "id": i.group("id"),
            "title": i.group("title"),
            "rating_num": i.group("rating_num"),
            "comment_num": i.group("comment_num")
        }


def main(num):  # 这个函数执行10次，每次爬取一页的内容
    url = 'https://movie.douban.com/top250?start=%s&filter=' %num
    response_html = getPage(url)
    ret = parsePage(response_html)  # ret就是生成器
    print(ret)
    f = open("move_info7", "a", encoding="utf8")

    for obj in ret:
        print(obj)
        data = str(obj)
        f.write(data + "\n")
    f.close()


com = re.compile(
    '<div class="item">.*?<div class="pic">.*?<em .*?>(?P<id>\d+).*?<span class="title">(?P<title>.*?)</span>'
    '.*?<span class="rating_num" .*?>(?P<rating_num>.*?)</span>.*?<span>(?P<comment_num>.*?)评价</span>', re.S)

count = 0
for i in range(10):
    main(count)
    count += 25
