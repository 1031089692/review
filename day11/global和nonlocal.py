# coding:utf-8

# a = 10    # 全局变量是不安全的, 不能随意修改。
# def func():
#     global a    # 1、可以把全局中的内容引入到函数内部 2、在全局创建一个变量。
#     a = 20
#     print(a)
# func()
# print(a)


# 需求是打印20
#def outer():
#     a = 10
#     def inner():
#         nonlocal a  # 寻找外层函数中离他最近的那个变量，如果到全局前一层还未找到，则报错。
#         a = 20
#     inner()
#     print(a)
# outer()


# 分析以下函数的最终打印结果
a = 1
def fun_1():
    a = 2
    def fun_2():
        nonlocal a
        a = 3
        def fun_3():
            a = 4
            print(a)
        print(a)
        fun_3()
        print(a)
    print(a)
    fun_2()
    print(a)
print(a)
fun_1()
print(a)
# 1-2-3-4-3-3-1


