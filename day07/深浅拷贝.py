# coding:utf-8


lst1 = ["语文", "数学", "英语", "化学"]
# lst2 = lst1[:]  #浅拷贝写法一。
lst2 = lst1.copy()  # 浅拷贝写法二。

lst1.append("体育")
print(lst1)
print(lst2)