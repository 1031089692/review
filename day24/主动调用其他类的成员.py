

class Base(object):
    def f1(self):
        print('5个鸡蛋')


class Foo(Base):
    def f1(self):
        print('三个鸡蛋')
        Base.f1(self)      # 主动调用父类的方法，这里要手动加上self。这里不继承也行（还有一个方法，使用super().f1() ，但是需要继承）



