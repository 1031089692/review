# coding:utf-8
import threading

# ##################线程的基本使用########################


# def func(arg):
#     print(arg)
#
#
# t = threading.Thread(target=func, args=(11,))
# t.start()
#
# print(123)


#########################################################
'''
主线程默认等子线程执行完毕再结束。
可以使用setDeamon(True)更改。更改之后，主线程不会等待，主线程终止则所有子进程也终止。
'''
import time
#
#
# def func(arg):
#     time.sleep(5)
#     print(arg)
#
#
# t = threading.Thread(target=func, args=(11,))
# t.setDaemon(True)
# t.start()
#
# time.sleep(3)
# print(123)


###################################################################
'''
join() 可以控制主线程等待子线程(最多等待时间)
'''
# def func(arg):
#     time.sleep(1)
#     print(arg)
#
#
# print('创建子线程t1')
# t1 = threading.Thread(target=func, args=(3,))
# t1.start()
# t1.join(2)
#
# print('创建子线程t2')
# t2 = threading.Thread(target=func, args=(9,))
# t2.start()
# t1.join(2)


###################################################################
'''
展示执行当前函数的线程名称
'''
# def func(arg):
#     t = threading.current_thread()
#     name = t.getName()
#     print(name, arg)
#
#
# t1 = threading.Thread(target=func, args=(3,))
# t1.setName('lq1')
# t1.start()
#
# t2 = threading.Thread(target=func, args=(9,))
# t2.setName('lq2')
# t2.start()
#
# print(123)


###################################################################
'''
线程本质
start的本质不是开始运行线程，而是通知cpu可以进行调度。所以在cpu非空闲状态时，下面例子
可能会先打印123。
'''
def func(arg):
    print(arg)


t1 = threading.Thread(target=func, args=(3,))
t1.start()
print(123)