# coding:utf-8

# 遍历文件夹，打印所有文件和普通文件的文件名
import os
def fun(filepath, n):
    #  1、拿到这个文件夹
    files = os.listdir(filepath)
    #  2、拿到每一个文件名
    for file in files:  # 文件名
        #  3、获取到路径
        f_d = os.path.join(filepath, file)
        #  4、判断是否是文件夹
        if os.path.isdir(f_d):
            #  5、如果是文件夹，再来一遍
            print("\t"*n, file, ":")  # 打印文件名
            fun(f_d, n+1)
        else:
            print("\t"*n, file)  # 打印文件名


# fun("/Users/liuqiang/Desktop/interface_case", 0)

# 对于一个list需要多次进行查询数据。请实现一个时间复杂度和空间复杂度最低的查找
lst = [6, 5, 7, 8]
lst2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in lst:    # 对需要查数据的列表的每一项的值进行遍历(注意不是遍历索引)
    lst2[i] = 1  # 在lst中查到的值换传承lst2中对应的索引，修改为1。
print(lst2)
