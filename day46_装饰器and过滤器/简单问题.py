# coding:utf-8


# 一个一开始没想明白的问题。关于inner的返回值的问题。

def foo():
    def inner(func):
        a = 2
        func()
    return inner


@foo()
def index():
    a = 1
    return a



def test():
    a = index
    print(a)


test()