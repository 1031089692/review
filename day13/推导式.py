# coding:utf-8

# lst = []
# for i in range(1, 16):
#     lst.append("python"+str(i))
# print(lst)
#
# # 推导式:用一句话来生成一个列表
# lst = ["python"+str(j) for j in range(1,16)]
# print(lst)
#
# # 语法:[结果 for循环 判断]
# # 如:打印奇数
# lst = [i for i in range(100) if i % 2 == 1]
# print(lst)
#
# # 100以内能被3整除的数的平方
# lst = [i*i for i in range(100) if i % 3 == 0]
# print(lst)

# 寻找名字中带有两个e的人的名字
# names = [['Tom', 'billy', 'Jefferson'], ['Alice', 'Eva', 'Jennifer']]
# # 原始算法：
# lst = []
# for name in names:
#     for el in name:
#         if el.count('e') == 2:
#             lst.append(el)
# print(lst)
# # 推导式
# lst = [el for name in names for el in name if el.count('e') == 2]
# print(lst)

# 字典推导式 语法{k:v for循环 条件筛选}
# [11, 22, 33, 44] => {0:11, 1:22, 2:33, 3:44}
# lst = [11, 22, 33, 44]
# dic = {i: lst[i] for i in range(len(lst))}
# print(dic)


# 将下面字典的k和v互换
# dic = {"jj": "林俊杰", "jay": "周杰伦"}
# dic2 = {j: i for i, j in dic.items()}
# print(dic2)

# 集合推导式一样
