# coding:utf-8
import time
import random


# 数字验证码
# def verificationCode(n=6):
#     str1 = ''
#     for i in range(n):
#         a = random.randint(0, 9)
#         str1 += str(a)
#     return str1
#
#
# a = verificationCode(6)
# print(a)


# 整合
def verificationCode2(n=6, alpha=True):
    str2 = ''
    for i in range(n):
        num = random.randint(0, 9)
        if alpha:
            alpha_upper = chr(random.randint(65, 90))   #找到a-z在ascii表的位置区间，然后用chr转换
            alpha_lower = chr(random.randint(97, 122))
            num = random.choice([num, alpha_lower, alpha_upper])
        str2 += str(num)
    return str2


b = verificationCode2(4, alpha=False)
print(b)
# 时间戳-结构化-格式化
'''
查看20000000时间戳时间表示的年月日
'''
struct_t = time.localtime(20000000)
print(struct_t)
print(time.strftime('%Y%m%d', struct_t))