# coding:utf-8
import time
import threading

n = 10
lock = threading.RLock()


def task(i):
    lock.acquire()  # 加锁
    global n
    print('当前线程', i, '读取到的n值为：', n)
    n = i
    time.sleep(1)
    print('当前线程', i, '修改n值为：', n)
    lock.release()    # 释放锁


for i in range(10):
    t = threading.Thread(target=task, args=(i,))
    t.start()