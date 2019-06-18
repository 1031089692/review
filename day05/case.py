# coding:utf-8

# 将下面的三个元素用_拼接成字符串
# li = ["alex", "eric", "rain"]
# a = ''
# for i in li:
#     a = a + i + '_'
# print(a[:-1])


# 将100以内的所有偶数放入一个列表(这里用步长更简单一点)
# li2 = []
# for i in range(101):
#     if i % 2 ==0:
#         li2.append(i)
# print(li2)


# 输入一段话，如果包含li列表的敏感字段，则用*全部替换
# li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
#
# str_input = input("请输入内容:")
# li2 = []
# for i in li:
#     if i in str_input:
#         str_input = str_input.replace(i, "*" *len(i))   #*len(i)是为了替换成对应数量的*
# li2.append(str_input)  # 全部放入一个列表这样能全部展示。
# print(li2)


# 循环打印列表中的每个元素，如果遇到列表则再循环打印出他的元素,如果有大写，全部换成小写。
# li = [1, 3, 4, "alex", [3, 7, 8, "TaiBai"], 5, "RiTiAn"]
# for i in li:
#     if type(i) == list:
#         for el in i:
#             if type(el) == str:
#                 print(f'"{el.lower()}"')
#             else:
#                 print(el)
#     else:
#         if type(i) == str:
#             print(f'"{i.lower()}"')    # f'"{}"'  固定格式。3.6版本后增加的。格式化输出
#         else:
#             print(i)


# 用户循环输入如"张三_95"这样格式的分数数据，按q退出。最后打印分数平均值
li = []
while 1:
    str_input = input("请输入姓名和分数(格式：张三_44)，最后输入Q退出:")
    if str_input.lower() == 'q':
        break
    else:
        ret = str_input.split('_')
        li.append(ret[1])  # 切片之后把分数放入列表

sum_num = 0
for i in li:
    sum_num = sum_num + int(i)
print(sum_num/len(li))