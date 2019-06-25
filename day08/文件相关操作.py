# coding:utf-8

# 如果需要反复查询，如果不移动光标，就会出问题。(后面会查不到)
# f = open("test3", mode="r", encoding="utf-8")
# for line in f:
#     print(line.strip())
# f.seek(0)
# for line in f:
#     print(line.strip())
# f.close()

# seek(0) 开头   seek(0,2)末尾。    seek的两个参数。第一个是偏移量(byte)，第二个是地址，0代表最前面，1代表当前位置，2表示结尾。


# tell()打印光标的位置(byte)


# truncate()
f = open("test3", mode="w", encoding="utf-8")
f.write("这是一条测试语句")
f.seek(9)   # 将光标移动到第三个汉字后面
print(f.tell())
f.truncate()  # 从文件开头截断到光标位置。如果给了参数，则表示从头截断到参数位置。
f.close()


