# coding:utf-8
import socket
import os
import json
import struct
import hashlib
sock = socket.socket()
sock.connect(('127.0.0.1', 9999))


while True:
    cmd = input("请输入命令:")
    if cmd == 'exit':
        break

    action, filename = cmd.strip().split(" ")
    filesize = os.path.getsize(filename)
    if action == 'put':
        file_info = {
            "action": action,  # put
            "filename": filename,  # 文件名
            "filesize": filesize,  # 文件大小
        }
        file_info_json = json.dumps(file_info).encode('utf8')
        ret = struct.pack('i', len(file_info_json))
        print(len(ret))

        # 发送file_info_json的打包长度
        sock.send(ret)
        # 发送file_info_json字节串
        sock.send(file_info_json)

        md5 = hashlib.md5()
