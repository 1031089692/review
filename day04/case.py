# coding:utf-8

# 题目：做一个基础的两个数的加法计算器
# a = input("请输入要计算的内容：")
# lis = a.split("+")
# print(int(lis[0])+int(lis[1]))

# 题目2：做一个多位数不固定的加法计算器


# 题目3：计算输入的内容中有多少个整数
# zs = 0
# content = input("请输入内容：")
# for i in content:
#     if i.isdigit():  # 判断是否为整数
#         zs = zs + 1
# print(zs)


# 计算1-2+3-4+5....+99中除了88以外所有数的总和
# sum1 = 0
# count = 1
# while count <= 99:
#     if count == 88:
#         count = count + 1
#         continue
#     if count % 2 == 0:
#         sum1 = sum1 - count
#     else:
#         sum1 = sum1 + count
#     count += 1
# print(sum1)


# 输入一个字符串。要求判断在这个字符串中大写字母，小写字母。数字，其他字符共出现多少次，并输出出来。
# content = input("请输入一句话：")
# daxie = 0
# xiaoxie = 0
# shuzi = 0
# other = 0
# for c in content:
#     if c.isupper():
#         daxie += 1
#     elif c.islower():
#         xiaoxie += 1
#     elif c.isdigit():
#         shuzi += 1
#     else:
#         other += 1
# print("大写字母有%s" % daxie, "小写字母有%s" % xiaoxie, "数字有%s" % shuzi, "其他有%s" % other)

# format简单应用
name = input("请输入你的名字：")
location = input("请输入地点：")
hobby = input("请输入爱好")
print("敬爱可亲的{}最喜欢在{}{}".format(name, location, hobby))

