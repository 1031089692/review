# coding:utf-8

# 枚举(后面的括号里面不写数字就跟索引一样，加数字就从该数字开始算起。)
lst = ["语文", "数学", "英语", "物理", "化学"]
for index, el in enumerate(lst, 100):
    print(index, el)
