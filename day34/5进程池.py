# coding:utf-8
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import time


def task(arg):
    time.sleep(2)
    print(arg)


# 创建一个线程池(最多5个线程)
pool = ProcessPoolExecutor(5)

for i in range(40):
    # 去线程池申请一个线程，让线程执行task函数
    pool.submit(task, i,)