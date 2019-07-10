# coding:utf-8

import re
s = '<a>wahaha</a>'
ret = re.search('<(\w+)>(\w+)</(\w+)>',s)
print(ret.group())  # 所有的结果
print(ret.group(1))
print(ret.group(2))
print(ret.group(3))

# findall
# python正则的默认分组优先和取消分组优先：(这个和正则本身无关)
# s = '<a>wahaha</a>'
# ret = re.findall('>(\w+)<',s)
# print(ret)   # 预期：>wahaha<   实际：wahaha  就是分组优先
# ret2 = re.findall('>(?:\w+)<',s)  #组内最前面加上?:表示取消分组优先
# print(ret2)   # 正常打印


'''
关于分组：
    1、对于正则表达式来说，有些时候我们需要进行分组，来整体约束某一组字符出现的次数
    2、对于python来说，分组可以帮助我们更好更精准的找到真正需要的内容
'''

# split
ret3 = re.split('\d+','john23faker27chuang50')  # 切割的内容不会保留
ret4 = re.split('(\d+)','john23faker27chuang50')  # 切割的内容会保留
print(ret3)
print(ret4)


# 分组命名，使用前面的分组 要求使用这个名字的分组和掐面同名分组中的内容匹配的必须一致。(用python也可以直接实现)
s = '<a>wahaha</a>'
pattern = '<(?P<tab>\w+)>(\w+)</(?P=tab)>'
ret = re.search(pattern, s)
print(ret)
