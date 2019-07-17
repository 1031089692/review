# coding:utf-8

'''
封装
'''

# 优化版本（参数的打包）
class Loy:

    def __init__(self, a, b, c):
        self.n1 = a
        self.n2 = b
        self.n3 = c

    def testmethod1(self):
        data = '%s%s%stest1' % (self.n1, self.n2, self.n3)
        print(data)

    def testmethod2(self):
        data = '%s%s%stest2' % (self.n1, self.n2, self.n3)
        print(data)

    def testmethod3(self):
        data = '%s%s%stest3' % (self.n1, self.n2, self.n3)
        print(data)


obj = Loy('我自己', '今天', '去打牌')
obj.testmethod1()
obj.testmethod2()
obj.testmethod3()


# 原始版本


class Loy2:

    def testmethod1(self, name, data, gender):
        data = '%s%s%stest1' % (name, data, gender)
        print(data)

    def testmethod2(self, name, data, gender):
        data = '%s%s%stest2' % (name, data, gender)
        print(data)

    def testmethod3(self, name, data, gender):
        data = '%s%s%stest3' % (name, data, gender)
        print(data)


obj1 = Loy2()
obj1.testmethod1('别人', '明天', '上班')
obj1.testmethod2('别人', '明天', '上班')
obj1.testmethod3('别人', '明天', '上班')