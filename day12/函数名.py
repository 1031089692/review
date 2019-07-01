# coding:utf-8


# 函数名可以作为参数传递给函数

def my():
    print("我是my")


def proxy(fn):
    print("在处理之前")
    fn()
    print("在处理之后")


proxy(my)

