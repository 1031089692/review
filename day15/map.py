# coding:utf-8

# map:映射函数 语法:map(function,iterable)

# 简单例子如下：
lst = [1, 2, 4, 5, 7, 22]
def fun(el):
    return el**2
m = map(fun,lst)
print(list(m))