# coding:utf-8


# def func():
#     print("哇哈哈")
#     yield 1   # return 和 yield都可以返回数据
#     print("呵呵呵")
#
#
# gen = func()  # 不会执行函数
# print(gen)   # 打印的生成器的地址
# ret = gen.__next__()
# print(ret)
# gen.__next__()


#  函数中如果有yield 这个函数就是生成器函数,生成器函数()获取的是生成器，这个时候不会执行函数
# yield: 类似于return,可以返回数据,但是yield不会彻底中断函数,分段执行函数
# gen.__next__() 执行函数,执行到下一个yield。


# 举例子
# def order():
#     lst = []
#     for i in range(10000):
#         lst.append("衣服"+str(i))
#     return lst
# ll = order()


# def order2():
#     for i in range(10000):
#         yield "衣服"+str(i)
# g = order2()  # 获取生成器
# a = g.__next__()
# print(a)
# 以上两个order函数对于内存的占用一目了然。


# send()和__next__()是一样的,可以执行到下一个yield,可以给上一个yield位置传值
def func():
    print("这是第一区间")
    a = yield 123
    print(a)
    print("这是第二区间")
    b = yield 456
    print(b)
    print("这是第三区间")
    c = yield 789
    print(c)
    print("这是第四区间")
    yield 000   # 最后收尾一定是yield,且最后一个yield不能传值

g = func()
print(g.__next__())  # 没有上一个yield 所以不能使用send() 开头必须是__next__()
print(g.send("土豆"))
print(g.send("凉薯"))
print(g.send("马铃薯"))
