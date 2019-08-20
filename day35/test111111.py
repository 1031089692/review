# coding:utf-8


class A:
    def show(self):
        print('base show')


class B:
    def show(self):
        print('derived show')



obj = B()
obj.__class__ = A
obj.show()