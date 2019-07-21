# 区分实例变量和类变量
# 通过题目加深理解
class StarkConfig(object):

    def __init__(self):
       self.list_display = []

    def get_list_display(self):
        self.list_display.insert(0, 33)
        return self.list_display


class RoleConfig(StarkConfig):
    list_display = [11, 22]


s1 = StarkConfig()    # 需要理解。这里的list是实例变量而不是类变量。

result1 = s1.get_list_display()
result2 = s1.get_list_display()



'''
------------------------------------------------------
'''
class StarkConfig2(object):
    list_display = []

    def get_list_display(self):
        self.list_display.insert(0, 33)
        return self.list_display


class RoleConfig2(StarkConfig):
    list_display = [11, 22]


s1 = RoleConfig2()
s2 = RoleConfig2()


result3 = s1.get_list_display()
print(result1)

result4 = s2.get_list_display()
print(result2)

