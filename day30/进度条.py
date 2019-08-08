# coding:utf-8
import time


def func(size,total_size):
    val = int(size/total_size * 100)
    time.sleep(0.1)
    print('\r%s%%' % val, end='')


for i in range(101):
    func(i, 100)
