# coding:utf-8

lst = []
with open("2019-06-25.log", mode="r", encoding="utf-8") as f:
    first = f.readline().strip().split(",")
    for line in f:
        dic = {}  # 每一行一个字典
        ls = line.strip().split(",")   # strip去除空白，split用","切片，生成列表。
        for i in range(len(first)):
            dic[first[i]] = ls[i]
        lst.append(dic)
print(lst)


