# coding:utf-8
import re
'''
从"1-2*(60+(-40.35/5)-(-4*3))"中取整数
'''
ret = re.findall("\d+\.\d+|\d+",'1-2*(60+(-40.35/5)-(-4*3))')
print(ret)  # 加上个筛选小数的条件
ret2 = re.findall("\d+\.\d+|(\d+)",'1-2*(60+(-40.35/5)-(-4*3))')
print(ret2)  # 设置整数分驻优先，小数不显示
ret2.remove('')
print(ret2)