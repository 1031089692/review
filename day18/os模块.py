# coding:utf-8
import os

# os.makedirs('test1') 创建文件夹
# os.rmdir('test1')  删除文件夹


# os.listdir / os.path.join
file_lst = os.listdir('/Users/liuqiang/PycharmProjects/review/day18')
for path in file_lst:
    print(path)  # 打印文件名
    print(os.path.join('/Users/liuqiang/PycharmProjects/review/day18',path))  # 打印路径



# ----暂时没什么用，先看看
