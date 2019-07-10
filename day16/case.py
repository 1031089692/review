# coding:utf-8

# 利用sorted对下面列表的数据按照value进行排序
a = [{'mm': 222}, {'mm': 333}, {'mm': 111}]

b = sorted(a, key=lambda el: el['mm'], reverse=True)
print(b)


# 斐波拉契数列(1、计算第400个数，2、不超过4000000的最大的值是第几个数)

# 匹配年月日
# ^[1-9]\d{0,3}-(1[0,2]|0?[1-9])-(3[01]|[1,2]\d|0?[1-9])$