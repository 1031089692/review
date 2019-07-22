# coding:utf-8

# 自定义异常： 1、自定义异常  2、主动抛出异常  3、 捕获异常


class MyException(Exception):
    def __init__(self, code , msg):
        self.code = code
        self.msg = msg


try:
    raise MyException(1000, '操作异常')


except MyException as obj:
    print(obj, 111)