# coding:utf-8

# 一个函数。两个参数。一个参数是个数组。第二个参数是一个数字。输出一个数组，为原数组中不包含第二个参数的其他所有数据
# a = [1,2,3,4,5]
# b = 5
# c = []
# for i in a:
#     if b != a[i]:
#         c.append(b)
# print(c)


# 返回一个整数的二进制中等于1的位数。  ---已完成
def count_bits(n):
    # n = bin(n).replace('0b', '')
    n = bin(n)
    print(n)
    count = 0
    for i in n:
        if i == '1':
            count += 1
        else:
            pass
    print(count)
    return count


# 给定一个数组，找出出现 奇数次的 整数

def find_id(seq):
    b = {}
    for i in seq:
        b.get(i)
        if None:
            b[i] = 0
        else:
            pass
    print(b)


find_id([0, 1, 0])



# 思路：循环遍历，把a列表的数据以字典的形式存入b列表(数据为key，出现次数为value)
# a = [0, 1, 0]
# b = {}
# for i in a:
#     print(i)
#     b.get(i)
#                                            
#     b[i] = 0
#
# print(b)