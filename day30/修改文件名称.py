# coding:utf-8
import os
import shutil

# py2 + win ：报错
os.rename('xx','xx')


# 改文件名和文件夹名都可以，py2+py3都不报错
shutil.move('xx','xx')