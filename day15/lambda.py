# coding:utf-8


# 普通的正常的函数
def func(n):
    return n*n


# 写成匿名函数,语法:lambda 参数:返回值
a = lambda n: n*n

# lambda返回多个参数需写成元祖的格式
b = lambda x, y: (x, y)   # 正确格式


# 匿名函数，给函数传递2参数，返回最大值
c = lambda *args: max(args)
print(c(1, 2))
