# coding:utf-8

# 一个函数。两个数组参数。输出一个数组，为第一个数组中数组中不包含第二个数组参数的其他所有数据   ---已完成
def array_diff2(a, b):
    c = []
    if len(b):  # 如果b不为空
        z = [x for x in a if x not in b]  # 拿到b没有，a有的数据。
        c = z
    else:   # b为空
        for i in a:
            c.append(i)
    return c


# 返回一个整数的二进制中等于1的位数。  ---已完成
def count_bits(n):
    # n = bin(n).replace('0b', '')
    n = bin(n)
    print(n)
    count = 0
    for i in n:
        if i == '1':
            count += 1
        else:
            pass
    print(count)
    return count


# 给定一个数组，找出出现 奇数次的 整数    ----已完成
'''
先循环一次参数，把所有数据存到一个字典，参数为key，出现次数为value。
然后遍历字典，把value为奇数的全部拿出来返回
'''


def find_id(seq):
    b = {}
    c = []
    for i, val in enumerate(seq):
        if b.get(val) == None:
            b[val] = 1
        else:
            b[val] += 1
    for i, val in b.items():   # i:key  val:value
        if val % 2 != 0:
            c.append(i)
    print(c)
    return c


# 给定一个字符串 将每个单词的首字母大写。   -----未完成
'''
思路：不使用title函数，遍历字符串。下标等于0的字符upper。下标的value=空白的。当前下标+1的字符upper
'''


def to_jaden_case(string):
    for i, val in enumerate(string):
        if i == 0:
            a = val.upper()
            string = string.replace(val, a)
        if val == ' ':
            print(i, val)
            print(string[i+1], string[i+1].upper())
            string = string.replace(string[i+1], string[i+1].upper())
            print(string)


# to_jaden_case("how can mirrors be real if our eyes aren't real")


# 入参为一个数组。如果为空。返回固定样式。参数长度为1，2，3和大于三分别给一个样式。 # 已完成
def like(str):
    if len(str) == 0:
        return("no one likes this")
    elif len(str) == 1:
        return("{} likes this".format(str[0]))
    elif len(str) == 2:
        return("{} and {} like this".format(str[0], str[1]))
    elif len(str) == 3:
        return("{}, {} and {} like this".format(str[0], str[1], str[2]))
    else:
        le = len(str)-2
        return("{},{} and {} others like this".format(str[0], str[1], le))


# 将字符转换为驼峰大小写
def to_camel_case(text):
    for i, val in enumerate(text):
        if val == '-' or val == '_':
            print(i)
        else:
            print(666)

to_camel_case('asdqw_sd-dasd')
