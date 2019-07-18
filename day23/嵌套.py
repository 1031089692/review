# coding:utf-8


class School(object):
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def speech(self):
        print('上课')


obj1 = School('清华大学', '北京')
obj2 = School('普林斯顿大学', 'USA')


class Teacher(object):
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.school = None


t1 = Teacher('王二狗', 19, 10000)
t2 = Teacher('李狗蛋', 25, 20000)

t1.school = obj1
t2.school = obj2

print(t1.school.address, t1.school.name)