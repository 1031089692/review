# coding:utf-8
import os


# 需求。将test4文件中的john换成liu
with open("test4", mode="r", encoding="utf-8") as f1,\
    open("test4_副本", mode="w", encoding="utf-8") as f2:

    for line in f1:
        line = line.replace("john", "liu")
        f2.write(line)

os.remove("test4")  # 删除文件
os.rename("test4_副本", "test4")