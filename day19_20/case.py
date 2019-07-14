# coding:utf-8
import os
import random
'''
1、
验证码:
    生成4位/6位数字验证码
    生成6位数字+字母验证码(区分大小写)

2、发红包:
    红包数量+钱数
    拼手气红包

3、写一个copy文件函数，接受两个参数，一个源文件位置，一个目标位置

4、计算器（加减乘除小括号小数负数）

5、写一个登陆。判断是否有注册，如果有注册，账号密码校验成功之后提示登陆成功。如果没有注册，提示注册（字典存数据），注册完成提示登陆。然后
登陆成功之后提示登陆成功。  ----这个我写过了。不重复写了。（代码量大，逻辑很简单）
'''

'''
1、获取源文件的绝对路径
2、判断目标文件是否为目录，如果不是目录，继续进入下一层
3、如果是文件。首先判断是否有同名文件，排除之后判断是否是py文件
4、如果是py文件就copy
'''


# copy
def copy(path1, path2):
    filename = os.path.basename(path1)   # 拿到源文件的绝对路径
    if os.path.isdir(path2) and os.path.isdir(path2):        # 判断是否为目录
        path2 = os.path.join(path2, filename)
        if os.path.exists(path2):print('已有同名文件')    # exists:判断文件路径是否存在，已存在的话print
        with open(path1, 'rb') as f1, open(os.path.join(path2, filename), 'wb') as f2:
            content = f1.read()
            f2.write(content)


# 发红包
def red_packet(money, num):
    money = money * 100  # 先转换成分，然后取整数
    ret = random.sample(range(1, money), num-1)  # sample()可以从指定的序列中，随机的截取指定长度的片断,
    ret.sort()  # 排序
    ret.insert(0, 0)  # 前面的0是索引， 后面的0是插入0
    ret.append(money)   # 结尾追加money
    for i in range(len(ret)-1):
        yield (ret[i+1] - ret[i])/100


ret_g = red_packet(100, 10)
for m in ret_g:
    print(m)

'''
思路：
    1、先转换成分取整数，最后转成元，可以正常保留两位小数，省了很多事儿。
    2、因为要分等num份，所以要sample的次数为num-1。
    3、排序可避免取值为负的问题。然后取值应该是sample的列表中每后一位减去前一位的值，这样全部加起来才是刚好等于money数量
    所以这里首尾要加上0和money
'''