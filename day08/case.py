# coding:utf-8

# 用户输入一个三位数，判断这个数是否为水仙花数。水仙花数是一个三位数，三位数的每一位的三次方的和还等于这个数
# 如153 = 1*3+5*3+3*3
# input_num = input("请输入一个三位数的数字：")
# s = 0
# for i in input_num:
#     s = int(i) ** 3 + s
#
# if int(input_num) == s:
#     print("是水仙花数")
# else:
#     print("不是水仙花数。")


# 从0-36随机打印7个数。要求不能重复。
# from random import randint
# s = set()
# while len(s) < 7:
#     r = randint(1, 36)
#     s.add(r)
# print(s)


# 基础冒泡排序
# for循环做法
# lst = [3, 5, 1, 4, 2, 3, 6, 9]
# n = 0
# for b in range(0, len(lst)):   # 外循环控制次数
#     for a in range(0, len(lst)-1):  # 内循环len-1防止索引越界。
#         if lst[a] > lst[a+1]:
#             lst[a], lst[a+1] = lst[a+1], lst[a]
# print(lst)

# while循环做法
# lst = [3, 5, 1, 4, 2, 3, 6, 9]
# count = 0
# while count < len(lst):  # 控制次数
#     i = 0
#     while i < len(lst)-1:
#         if lst[i] > lst[i+1]:
#             lst[i], lst[i+1] = lst[i+1], lst[i]
#         i = i + 1
#     count = count + 1
# print(lst)

