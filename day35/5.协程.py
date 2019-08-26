# coding:utf-8
import greenlet


def f1():
    print(11)  # 1、打印这里
    gr2.switch()
    print(22)   # 3、打印这里
    gr2.switch()


def f2():
    print(33)   # 2、打印这里
    gr1.switch()
    print(44)    # 4、打印这里


gr1 = greenlet.greenlet(f1)  # 协程gr1
gr2 = greenlet.greenlet(f2)   # 协程gr2
gr1.switch()