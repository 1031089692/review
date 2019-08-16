# coding:utf-8
import threading
import time

lock = threading.BoundedSemaphore(3)


def func(arg):
    lock.acquire()
    print(arg,)
    time.sleep(1)
    lock.release()


for i in range(10):
    t = threading.Thread(target=func, args=(i,))
    t.start()