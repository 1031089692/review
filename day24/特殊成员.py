

class Foo(object):

    def __new__(cls, *args, **kwargs):
        """
        创建一个空对象
        :param args:
        :param kwargs:
        :return:
        """
        print(2)
        return object.__new__(cls)

    def __init__(self, a1, a2):
        # 为一个空对象进行数据的初始化
        self.a1 = a1
        self.a2 = a2

    def __call__(self, *args, **kwargs):
        print(1111)

    def __getitem__(self, item):
        print(item)
        return 8

    def __setitem__(self, key, value):
        print(key, value, 1111111)

    def __delitem__(self, key):
        print(key)

    def __add__(self, other):
        return self.a1 + other.a1

    def __enter__(self):
        print('进入文件')
        return 999

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(222)


# 1.类名() 自动执行__init__
obj = Foo(1, 2)
# 2.对象() 自动执行__call__
obj()
# 3.对象[] 自动执行 __getitem__
ret = obj['语文']
print(ret)
# 4.对象['xxx']=123 自动执行 __setitem__  # 无返回值
obj['k1'] = 123
# 5.del 对象['xxxx'] 自动执行 __delitem__
del obj['uuu']
# 6.对象+对象   自动执行 __add__
obj1 = Foo(1, 2)
obj2 = Foo(3, 4)
ret = obj1 + obj2
print(ret)
# 7.with 对象
obj3 = Foo(1, 2)
with obj as f:
    print(f)   # f就是enter的返回
    print('内部代码')
# 8.真正的构造方法  __new__  在实例化一个对象时，首先执行的是new，其次才是init
