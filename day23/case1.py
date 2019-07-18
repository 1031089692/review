# coding:utf-8

def test():
    for i in range(1,10):
        yield i

a = test()
print(type(a))
b = next(a)
print(b)
b = next(a)
print(b)
b = next(a)
print(b)
# b = a.__next__()
# print(b)
# b = a.__next__()
# print(b)
# b = a.__next__()
# print(b)
# b = a.__next__()
# print(b)
# b = a.__next__()
# print(b)
