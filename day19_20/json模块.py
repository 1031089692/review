# coding:utf-8
import json

dic = {'key': 'value', 'key2': 'value2'}
ret = json.dumps(dic)  # 序列化 字典转json
print(dic, type(dic))
print(ret, type(ret))

res = json.loads(ret)  # 反序列化 json 转字典
print(res, type(res))


'''
1、如果字典的key是数字，则会强制转换成字符串，json.loads不会转回来
2、如果字典的value是一个元祖，则会强制转换成列表,json.loads不会转回
3、必须是键值对，否则报错。
4、如果字典的key是元祖则会报错:TypeError: keys must be a string

总结:
json能够处理的数据类型是非常有限的:字符串 列表 字典 数字
    且字典中的key只能是字符串
'''

# dumps和loads是操作内存，一般用于网络传输
# dump和load是操作文件，一般用于文件操作。

