# coding:utf-8
import threading
import time

lock = threading.RLock()
v = []


def func(arg):
    #lock.acquire()  # 加锁
    v.append(arg)
    time.sleep(0.01)
    m = v[-1]
    print(arg, m)
    #lock.release()   # 释放锁


for i in range(10):
    t = threading.Thread(target=func, args=(i,))
    t.start()   # start的本质不是开始运行线程，而是通知cpu可以进行调度。