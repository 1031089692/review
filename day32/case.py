# coding:utf-8

# 作业1 下面两个列表。一个每一项+1，一个每一项+100
import threading
v1 = [11, 22, 33]    # +1
v2 = [44, 55, 66]    # +100


def func(data, plus):
    for i in range(len(data)):
        data[i] = data[i] + plus


t1 = threading.Thread(target=func, args=(v1, 1))
t2 = threading.Thread(target=func, args=(v2, 100))
# 由于GIL锁的存在。所以这个多线程毛用没有


