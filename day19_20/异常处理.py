# coding:utf-8

try:
    pass
except (ValueError, IndexError):
    print("针对性错误的处理")
except Exception as e:
    print("未知错误的通用处理")
