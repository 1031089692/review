# coding:utf-8

# 可迭代对象可以使用__iter__()来获取迭代器
# 迭代器里面有__nexe__()
# s = '我在学习'
# it = s.__iter__()  # 获取迭代器
# print(dir(it))    # 迭代器里有__iter__ 还有__next__

# 1、不能反复，只能向下执行。
# 2、几乎不占用内存，节省内存
# 3、for循环
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())


# 迭代器模拟for循环
lst = ["语文", "数学", "英语", "物理", "化学"]
# for el in lst:
#     print(el)
it = lst.__iter__()  # 获取迭代器
while 1:
    try:
        el = it.__next__()  # 获取下一个元素
        print(el)
    except StopIteration:   # 处理错误
        break

# 判断是否是可迭代对象和是否是迭代器
from collections.abc import Iterable    # 可迭代对象
from collections.abc import Iterator    # 迭代对象

print(isinstance(it, Iterable))
print(isinstance(it, Iterator))