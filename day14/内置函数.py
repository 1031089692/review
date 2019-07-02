# coding:utf-8
lst = ['语文', '数学', '物理']

# it = lst.__iter__()
# print(it)
# print(it.__next__())
# print(it.__next__())

# it = iter(lst)  # 内部封装的就是__iter__()
# print(it.__next__())
# print(next(it))  # 内部封装的就是__next__()
#
#
# # 复数= 实数+虚数 3+2i
#
# print(bin(3))  # 3的二进制   0b二进制
# print(oct(5))  # 5的8进制    0o八进制
# print(hex(16))  # 16的16进制  0x十六进制 0123456789ABCDEF

'''
import base64
# encodewx = base64.b64encode('lq103108962'.encode('utf-8'))
# print(encodewx)
decodewx = base64.b64decode(encodewx).decode("utf-8")
print(decodewx)
'''

# zip
lst1 = ['语文', "数学", '英语']
lst2 = ['王老师', '李老师', '刘老师']
lst3 = ['单身', '已婚', '单身']
a = zip(lst1, lst2, lst3)
for el in a:
    print(el)