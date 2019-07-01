# coding:utf-8


# 判断输出
def extendList(val, list=[]):   # 默认值如果是可变的数据类型，每次使用的时候都是同一个。
    list.append(val)
    return list


list1 = extendList(10)
list2 = extendList(123, [])
list3 = extendList('a')

print('list1=%s' % list1)
print('list2=%s' % list2)
print('list3=%s' % list3)



