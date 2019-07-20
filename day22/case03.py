# 多态


class Base(object):
    def fun(self):
        print('这是一个基类')


class Foo(Base):
    def fun(self):
        Base.fun(self)
        print('这是派生类1')


class Foo2(Base):
    def fun(self):
        Base.fun(self)
        print('这是派生类2')


a = Base()
b = Foo()
c = Foo2()

a.fun()
b.fun()
c.fun()

'''
打印结果如下：
这是一个基类
这是一个基类
这是派生类1
这是一个基类
这是派生类2
'''