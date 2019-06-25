# coding:utf-8

# 写函数，检查获取传人列表或元祖对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者

#
# def jishu(lst):
#     lst2 = []
#     for i in range(len(lst)):
#         if i % 2 == 1:
#             lst2.append(lst[i])
#     return lst2
#
#
# a = jishu(lst=["语文", "数学", "英语", "物理", "化学"])
# print(a)


# 写函数，接收两个数字参数，返回比较大的那个数字


# def func(a, b):
#     return a if a > b else b
# 这里用三元表达式看起来比较简介。(表达式写中间，如果成立，返回左边，不成立，返回右边。)


# 写函数，检查传入字典的每一个value的长度，如果大于2。那么仅保留前两个长度的内容，并将新内容返回给调用者。
# def func(dic):
#     new_dict = {}
#     for k, v in dic.items():
#         if len(v) > 2:
#             s = v[0:2]
#             new_dict[k] = s
#         else:
#             new_dict[k] = v
#     return new_dict
#
#
# a = func(dic={"语文": "100", "数学": "90"})
# print(a)


# 用户用过输入这四个内容，然后将这四个内容传入到函数中，
# 此时接收到这四个内容，将内容追加到一个student_msg文件中


def funch(name, gender, age, edu):
    with open("student_msg", mode="a", encoding="utf-8") as f:
        f.write(name+"_"+gender+"_"+age+"_"+edu+"\n")


funch(name='john', gender='男', age='18', edu='本科')
