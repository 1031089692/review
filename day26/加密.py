# coding:utf-8

import hashlib

SALT = b'asdasd'


def md5(pwd):
    # 写入要加密的字节
    obj = hashlib.md5(SALT)   # 加盐 SALT
    obj.update(pwd.encode('utf-8'))

    # 获取密文
    v = obj.hexdigest()
    return v



# 本人的疑问。md5是不可逆的。那么解密就是通过对比已加密内容和明文的加密是否一致来判读的。那是不是还是要存明文的数据。