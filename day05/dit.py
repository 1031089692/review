# coding:utf-8

# python 3.6版本之后字典已经变成有序的了。3.5之前的没有

# 增
dic = {"xx": "xx", "名字": "刘强", "年龄": "23", "性别": "男", "爱好": "女"}
# dic['专业'] = '测试'    # 如果键在字典中就强制修改，如果键不在字典中就强制添加。
# dic.setdefault('目标', '测开')    # 如果键在字典中存在就不进行任何操作，如果不存在就进行添加。
# print(dic)

# 删
# pop
# dic.pop('爱好')
# print(dic)
# del
# del dic['性别']
# print(dic)
# del
# dic.clear()
# print(dic)
# popitem
# ret = dic.popitem()  # 说是说随机删除。实际我看到的都是固定删除结尾
# print(ret)  # 返回一个元祖。
# print(dic)


# 改
# dic['年龄'] = '25'    # 强制修改
# dic1 = {"名字": "而已", "年龄": "23", "性别": "男", "爱好": "女", "yy": "yy"}
# dic.update(dic1)  # update修改，两个字典数据都会存入，如果有同key的，value取最前面的字典的。
# print(dic)


# 查
# for循环查。默认查到key，当然也可以遍历value，或者item。
# for i in dic.values():
#     print(i)
# print(dic['姓名1'])     # 如果这个键没有，则会报错
# print(dic.get('姓名1', '查无此数据'))   # 如果没有这个键，则返回None。还可以自己定义找不到的时候的返回值。
# print(dic.setdefault('姓名2'))    # setdefault不仅可以用于增加，同样可以同来查询，就放一个key就行。如果没有，返回None


# 解构(解包)
a, b = (1, 2)  # 将后面解构打开按位置赋值给变量，支持str、list、tuple
print(a)
print(b)
