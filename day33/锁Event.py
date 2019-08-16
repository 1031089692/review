# coding:utf-8
import threading
import time

lock = threading.Event()


def func(arg):
    print('线程来了')
    lock.wait()   #加锁。全部卡住
    print(arg,)


for i in range(10):
    t = threading.Thread(target=func, args=(i,))
    t.start()


input('>>>>:')
lock.set()
input('>>>>:')