
# 类和对象可以作为字典的key

# class Start(object):
#
#     def __init__(self, num):
#         self.num = num
#
# a = Start(num=12)
# print(a.num)


# class AdminSite(object):
#     def __init__(self):
#         self._registry = {}
#
#     def register(self, k, v):
#         self._registry[k] = v
#
#
# site = AdminSite()
# print(len(site._registry))
# site.register('语文', '666')
# site.register('数学', '999')
# print(site._registry)
#

#判断打印结果1.0
class StarkConfig(object):

    def __init__(self, num):
        self.num = num

    def changelist(self, request):
        print(self.num, request)

    def run(self):
        self.changelist(999)


class RoleConfig(StarkConfig):

    def changelist(self, request):
        print(666, self.num)


class AdminSite(object):

    def __init__(self):
        self._registry = {}

    def register(self, k, v):
        self._registry[k] = v


site = AdminSite()
site.register('语文', StarkConfig(19))
site.register('数学', StarkConfig(20))
site.register('英语', RoleConfig(33))

for amd, row in site._registry.items():
    row.run()


# 判断打印结果2.0
# class UserInfo(object):
#     pass
#
#
# class Department(object):
#     pass
#
#
# class StarkConfig(object):
#
#     def __init__(self, num):
#         self.num = num
#
#     def changelist(self, request):
#         print(self.num, request)
#
#     def run(self):
#         self.changelist(999)
#
#
# class RoleConfig(StarkConfig):
#
#     def changelist(self, request):
#         print(666, self.num)
#
#
# class AdminSite(object):
#
#     def __init__(self):
#         self._registry = {}
#
#     def register(self, k, v):
#         self._registry[k] = v(k)
#
#
# site = AdminSite()
# site.register(UserInfo, StarkConfig)
# site.register(Department, StarkConfig)
#
# for amd, row in site._registry.items():
#     row.run()


# 总结：
'''
1、对象中封装了什么？
2、self到底是谁？

'''