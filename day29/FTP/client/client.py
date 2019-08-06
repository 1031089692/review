# coding:utf-8
import socket
import os
import json
sock = socket.socket()
sock.connect(('127.0.0.1', 8800))


while True:
    cmd = input("请输入命令:")

    action, filename = cmd.strip().split(" ")
    filesize = os.path.getsize(filename)

    file_info = {
        "action": action,
        "filename": filename,
        "filesize": filesize,
    }
    file_info = json.dumps(file_info).encode('utf8')
    sock.send(file_info)

    # 确认服务器接收到了文件信息
    code = sock.recv(1024).decode("utf8")
    if code == '200':
        # 发送文件数据
        with open(filename, 'rb') as f:
            for line in f:
                sock.send(line)


    else:
        print('服务器异常！')
