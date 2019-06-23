# coding:utf-8


# lst1 = ["语文", "数学", "英语", "化学"]
# # lst2 = lst1[:]  #浅拷贝写法一。
# lst2 = lst1.copy()  # 浅拷贝写法二。
#
# lst1.append("体育")
# print(lst1)
# print(lst2)

# 深入理解浅拷贝
lst3 = ["java", "golang", "php", "JavaScript", ["python核心编程", "python入门", "python深入浅出"]]
lst4 = lst3.copy()   # 对lst3进行浅拷贝。生成lst4。
lst3[4].append("玩转python")
print(lst3)
print(lst4)
# 可以看到两个list都添加了"玩转python"这个字段。这是因为从内存的角度来说。lst3[4]这个嵌套的列表是独立存放的，可以
# 理解为lst3[4]在lst3仅存放了一个标识符。在lst3中通过这个标识符找到lst3[4]。而我们添加"玩转python"这个数据其实是
# 添加到了lst[4]中，而不是lst3中。这就是为什么打印时两个列表都会展示添加了的原因(我们可以通过打印着两个嵌套的子列表
# 的内存地址来进行验证)


# 深入理解深拷贝。需先引入copy模块
