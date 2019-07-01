# coding:utf-8


# 闭包，在内层函数中访问外层函数的变量
# 闭包作用:
#     1、可以保护你的变量不受侵害
#     2、可以让一个变量常驻内存
def outer():
    a = 10
    def inner():
        print(a)
    inner()
outer()



def func():
    a = 10
    def inner():
        print(a)
    print(inner.__closure__)  # 如果打印的是None，不是闭包。如果不是None，就是闭包
func()
print(dir(str))   # dir查看xx类型的数据可以执行哪些方法。
