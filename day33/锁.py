# coding:utf-8
import threading
import time

lock = threading.Lock()
v = []


def func(arg):
    lock.acquire()
    v.append(arg)
    time.sleep(0.01)
    m = v[-1]
    print(arg, m)
    lock.release()


for i in range(10):
    t = threading.Thread(target=func, args=(i,))
    t.start()