# coding:utf-8

from types import MethodType, FunctionType


def check(arg):
    """
    检查arg是方法还是函数
    :param arg:
    :return:
    """
    if isinstance(arg, MethodType):
        print("arg是一个方法")
    elif isinstance(arg, FunctionType):
        print("arg是一个函数")
    else:
        print("不知道是啥")


# 敲黑板，是方法还是函数，与他写在哪里没有关系，与调用方有关系
class Foo(object):

    def f1(self):
        pass


obj = Foo()
print(obj.f1)   # 用对象去调用，那么就是一个方法
print(Foo.f1)   # 用类去调用，那么就是一个函数
