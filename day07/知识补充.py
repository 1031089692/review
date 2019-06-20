# coding:utf-8

# join将列表转换成字符串，每个元素之间用_拼接   join(可迭代对象)
#s = "_".join(["张三", "莉丝", "王五"])
#print(s)
# split将字符串转换成列表
#ss = '张三_莉丝_王五'
#print(ss.split("_"))


# 在不使用clear的情况下清空一个列表。
# lst = ["语文", "数学", "英语", "物理", "化学", "体育"]
# for i in lst:
#     lst.remove(i)
# print(lst)
'''
删除的时候发现剩余了一部分内容，原因是内部的索引在改变。需要把要删除的内容记录下来，然后
循环这个记录，删除原来的列表。
'''
lst = ["语文", "数学", "英语", "物理", "化学", "体育"]
new_list = []
for i in lst:
    new_list.append(i)
for i in new_list:
    lst.remove(i)
#print(lst)


# 再来一个例子。删除掉下面list中姓张的明星
lst2 = ["张国荣", "张学友", "张国立", "张曼玉", "张铁林", "刘德华"]
lst3 = []
# 删掉姓张的
for a in lst2:
    if a.startswith("张"):
        lst3.append(a)
for a in lst3:
    lst2.remove(a)
#print(lst2)
#print(lst3)


# 字典的循环删除
dic = {"姓名": "张三", "年龄": "28", "性别": "男"}
ls = []
for k in dic:
   ls.append(k)
for j in ls:
    dic.pop(j)
#print(dic)                       
# 综上，列表和字典都不能在循环的时候进行删除。字典在循环自身的时候不允许改变大小。


# 字典的fromkeys
ddd = {"apple": "苹果", "banana": "香蕉"}
# 首先fromkeys是返回新字典，对原来的字典没有影响
ret = dic.fromkeys("orange", "橘子")        #错误使用方法
ret2 = dict.fromkeys(["a", "b", "c"], ["1", "2", "3"])     #正确应该直接使用类名dict访问。
# 且仅适用于多key匹配同一个value。无法实现多key匹配多value(也就是说value是共享的)。
print(ret)
print(ret2)