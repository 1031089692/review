# coding:utf-8

lst = ["语文", "化学", "英语", "地理"]


def func(el):
    if el[0] == '语':
        return False  # 不想要的
    else:
        return True  # 想要的


f = filter(func, lst)  # 将lst中的每一项传递给func，所有返回True的都会被保留，返回False的不会
print("__iter__" in dir(f))  # 判断是否可以进行迭代
for le in f:
    print(le)


# 使用lambda优化：
k = filter(lambda el: el[0] != '语', lst)
for l in k:
    print(l)