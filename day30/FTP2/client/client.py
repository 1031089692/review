# coding:utf-8
import socket
import os
import json
import struct
import hashlib
sock = socket.socket()
sock.connect(('127.0.0.1', 8800))


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
        # 发送文件数据
        with open(filename, 'rb') as f:
            for line in f:
                sock.send(line)
                md5.update(line)
        data = sock.recv(1024).decode('utf8')
        if data == '200':
            print(md5.hexdigest())
            md5_val = md5.hexdigest()
            sock.send(md5_val.encode('utf8'))
            valid = sock.recv(1024).decode('utf8')
            if valid == '100':
                print('文件上传成功')
            else:
                print('文件上传失败!')
        else:
            print('服务器出错了!')
    else:
        print('请输入正常的命令')
