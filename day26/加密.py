# coding:utf-8

import hashlib
SALT = b'asdasd'


def md5(pwd):
    obj = hashlib.md5(SALT)   # 加盐 SALT
    obj.update(pwd.encode('utf-8'))

    # 获取密文
    v = obj.hexdigest()
    return v



