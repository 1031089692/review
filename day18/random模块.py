# coding:utf-8
import random


# 取随机小数
print(random.random())  # 取0-1之间的小数
print(random.uniform(1, 2))  # 取规定区间内的小数


# 取随机整数
print(random.randint(1, 2))  # [1,2]
print(random.randrange(1, 2))  # [1,2) 这个不顾尾
print(random.randrange(1, 200, 2))  # 第三个数代表步长，及没两个取一个，如2，就是全部奇数取随机数。


# 从一个列表中随机抽取值
l = ['a', 'b', (1, 2), 123]
print(random.choice(l))  # 固定随机取一个值，多次可能会重复
print(random.sample(l, 2))  #(数据源，取值量)两个参数。不可能出现重复数据


# 打乱一个列表的顺序
random.shuffle(l)    # 在原列表直接进行的修改，节省空间
print(l)
