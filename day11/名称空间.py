# coding:utf-8

# 关于作用域已经很属性了。这里复习下python的执行顺序
def outer():
    print("哈哈")
    def inner_1():
        print("呵呵")
        def inner_1_1():
            print("嘻嘻")
        inner_1_1()
        print("哄哄")
    def inner_2():
        print("嘿嘿")
    inner_2()
    inner_1()
outer()

# 打印顺序为:哈哈=>嘿嘿=>呵呵=>嘻嘻=>哄哄