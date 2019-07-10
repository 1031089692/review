# coding:utf-8
import time

'''
时间格式：
    1、'2018-05-20' --字符串数据类型  格式化时间
    2、结构化时间 --上下两种时间的转换
    3、1562641421.025376  --浮点型数据类型，以s为单位  时间戳时间
'''
print(time.time())
print(time.strftime('%Y-%m-%d %H:%M:%S'))