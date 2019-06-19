# coding:utf-8

# 编码

s = 'alex'
print(s.encode('utf-8'))  # 输出b'alex'，即bytes类型   # 编码 encode('utf-8') utf-8是指定编码类型
s = '饿了么'
print(s.encode("utf-8"))  # b'\xe9\xa5\xbf\xe4\xba\x86\xe4\xb9\x88'
print(s.encode("gbk"))    # b'\xb6\xf6\xc1\xcb\xc3\xb4'


# 解码(用什么格式编码，就用什么格式解码)
a = '饿了么'
a1 = a.encode('utf-8')
print(a1.decode('utf-8'))