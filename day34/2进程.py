# coding:utf-8
import multiprocessing


def task(arg):
    print(arg)


for i in range(10):
    p = multiprocessing.Process(target=task, args=(i, ))
    p.start()