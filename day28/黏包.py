# coding:utf-8


# 主要就是应用struct模块的pack和unpack两个方法。首先用pack对于字符串进行压缩，这样长度就固定了。然后接收后unpack解压缩，循环取值拼接
# 字符串就行了