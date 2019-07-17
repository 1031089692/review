# coding:utf-8

'''
继承
'''


# class Base:
#     def f2(self):
#         print('f2')
#
#
# class Foo(Base):
#     def f1(self):
#         print('f1')
#         self.f2()

#
# class Base:
#     def f1(self):
#         print('base.f1')
#
#     def f3(self):
#         self.f1()                #这里的self还是指向obj
#         print('foo.f3')
#
#
# class Foo(Base):
#     def f2(self):
#         print('foo.f2')
#         self.f3()
#
#
# obj = Foo()
# obj.f2()


# 判断打印结果 and why?
class Base1:
    def f1(self):
        print('base1.f1')
    def f2(self):
        print('base1.f2')


class Base2:
    def f1(self):
        print('base2.f1')
    def f2(self):
        print('base2.f2')
    def f3(self):
        print('base2.f3')
        self.f1()

class Foo(Base1, Base2):
    def f0(self):
        print('foo.f0')
        self.f3()


obj = Foo()
obj.f0()