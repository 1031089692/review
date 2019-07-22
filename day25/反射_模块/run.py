# coding:utf-8

from types import FunctionType
import handler
while True:
    print("""
    系统支持的函数有:
        1.f1
        2.f2
        3.f3
        4.f4
        5.f5
        6.f6
    """)
    val = input("请输入要执行的函数：")
    if hasattr(handler, val):
        func_or_val = getattr(handler, val)  # 根据字符串为参数，去模块中寻找与之同名的成员
        if isinstance(func_or_val, FunctionType):
            func_or_val()
        else:
            print(func_or_val)
    else:
        print('不存在输入的属性名')


# 总结。根据字符串为参数（第二个参数），去对象（第一个参数）中寻找与之同名的成员