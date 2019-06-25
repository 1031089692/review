# coding:utf-8

# *在这里表示接收位置参数的动态传参,接收到的是元祖。
# 顺序: 位置参数=>*args(arguments)=>默认值参数
# def chi(*food):  # 参数名是food *表示动态传参数
#     print(food)


# 关键字的动态传参,接收到的是字典。
# def chichi(**food):
#     print(food)
# chichi(good_food = "米饭", drink = "肥仔快乐水")


# 动态传参数最终顺序
# 位置参数，*args，默认值参数，**kwargs
# 以上参数可以随意搭配使用。


# 接收所有参数写法
# def func(*args, **kwargs):
#     print(args, kwargs)


# 形参:聚合
def func(*food):  # 聚合,位置参数
    print(food)
    lst = ["语文", "数学", "英语", "物理"]
    # 实参:打散
    func(*lst)  # 打散。把list,tuple,set,str进行迭代打散。
