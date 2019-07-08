# coding:utf-8
import re

# 查找
# findall ： 匹配所有 每一项都是列表中的一个元素
# ret = re.findall('\d+', '123qeqwesd234asdsdfsdf')
# print(ret)


# search : 只匹配从左到右的第一个，得到的不是直接的结果，而是一个变量，通过这个变量的group方法来获取结果。
# 如果没有匹配到，会返回None，此时使用group会报错。
# ret2 = re.search('\d+','asd123sdf43asd23')
# print(ret2)  # 打印的是内存地址，这是一个正则匹配的结果
# print(ret2.group())  #通过ret.group()来获取真正的结果


# match 从头开始匹配，相当于search中的正则表达式加上一个^


# 字符串处理的扩展
# split 切割
# s = 'john23faker27chuang50'
# ret3 = re.split('\d+',s)
# print(ret3)
#
# # sub替换 (正则，替换的结果，需要替换的内容，替换的次数)
# ret4 = re.sub('\d+', 'H', 'john23faker27chuang50', 1)
# print(ret4)

# subn 返回一个元祖，第二个元素是替换的次数


# re模块的进阶:
#compile  节省使用正则表达式解决问题的时间
#编译 正式表达式编译成字节码
# 在多次使用过程中，不会多次编译
ret = re.compile('\d+')  #已经完成编译了
print(ret)
res = ret.findall('asdasd123asaw234asd112')
print(res)
res2 = ret.search('asd123sdf444123qas')
print(res2.group())


#finditer  节省使用正则表达式解决问题的空间/内存
ret5 = re.finditer('\d+', 'asdasd123sdfsrt234dfgerdgr234')
for i in ret5:
    print(i.group())
