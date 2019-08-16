# coding:utf-8
import multiprocessing
import time
import queue

############################方式1：multiprocessing.Queue()###########################################
# q = multiprocessing.Queue()
#
#
# def task(arg):
#     q.put(arg)
#
#
# def run():
#     for i in range(10):
#         p = multiprocessing.Process(target=task, args=(i, ))
#         p.start()
#     while True:
#         v1 = q.get()
#         print(v1)
#
# run()


##########################方式2：multiprocessing.Manger()###############################################
m = multiprocessing.Manager()
dic = m.dict()


def task(arg):
    dic[arg] = 100


def run():
    for i in range(10):
        p = multiprocessing.Process(target=task, args=(i, ))
        p.start()

    input('>>>')
    print(dic.values())


if __name__ == '__main__':
    run()