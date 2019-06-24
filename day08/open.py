# coding:utf-8

# f = open("test", mode="r", encoding="UTF-8")   # 注意文件名的后缀，本身没有，读取的时候就不要加
# s = f.read()
# print(s)
# f.close()

# 文件路径：
# 1、绝对路径：从磁盘的根目录寻找，或者从互联网上寻找一个路径
# 2、相对路径(用得多)：相对于当前程序所在的文件夹


# 一行一行的处理数据
# f = open("test2", mode="r", encoding="utf-8")
# for line in f:
#     print(line.strip())    # strip去除多余的换行。
# f.close()


# 带w的，只要你操作了，就会清空源文件
# 如果文件不存在，会自动创建文件。
# f = open("test3", mode="w", encoding="utf-8")
# f.write("读写测试\n")
# f.write("读写测试2")
# f.flush()
# f.close()


# a模式。写的时候，换行需要手动控制
# f = open("test3", mode="a", encoding="utf-8")
# f.write("\n读写测试3")
# f.write("\n读写测试4")
# f.flush()
# f.close()


# rb, wb, ab, b=bytes.处理的是非文本文件。mode里如果有b，encoding就不能给了
# f = open("源文件路径", mode="rb")
# e = open("拷贝的路径", mode="Wb")
# for line in f:
#     e.write(line)
# f.close()
# e.flush()
# e.close()  # 到这里。非文本文件的复制就完成了


# r+。无论你读取了多少内容。光标在哪儿。写入的时候都是在结尾写入。如果读之前写入，则是在开头写入，且会覆盖之前的对应位置的部分数据。
# 最好用的读写同时存在的模式
# f = open("test3", mode="r+", encoding="utf-8")
# s = f.read(3)  # 读取三个字符。
# print(s)
# f.write("\nr+模式测试输入")  # 在末尾写入
# f.close()


# w+模式。w+模式写的话会覆盖原来的内容。所以很少用。(a+的话就是结尾追加，光标默认到结尾，其余都差不多)
f = open("test3", mode="w+", encoding="utf-8")
f.write("两个月系统的复习一遍python")  # 写完之后这时光标是在最后的，所以读取是为空的。需要移动光标
f.seek(0)  # 把光标移动到最前面
s = f.read()
print("读取的内容为：", s)
f.flush()
f.close()
