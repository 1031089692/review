# coding:utf-8
import socket
import json
import struct
import hashlib
sock = socket.socket()
sock.bind(('127.0.0.1', 8800))
sock.listen(5)

while True:
    print("server is working.......")
    conn, addr = sock.accept()
    while True:
        # 接收json的打包长度
        file_info_lenght_pack = conn.recv(4)
        file_info_lenght = struct.unpack('i', file_info_lenght_pack)[0]

        # 接收json字符串
        file_info_json = conn.recv(file_info_lenght).decode('utf8')
        file_info = json.loads(file_info_json)

        action = file_info.get('action')
        filename = file_info.get('filename')
        filesize = file_info.get('filesize')

        md5 = hashlib.md5()

        # 循环接收文件
        with open("put/"+filename, "wb") as f:
            recv_data_length = 0
            while recv_data_length < filesize:
                data = conn.recv(1024)
                recv_data_length += len(data)
                f.write(data)
                md5.update(data)
                print("文件总大小:%s,已成功接收%s" % (filesize, recv_data_length))
        print('接收成功')
        conn.send(b'200')
        print(md5.hexdigest())
        md5_val = md5.hexdigest()   # 服务端的md5
        client_md5 = conn.recv(1024).decode('utf8')     # 接收用户端的md5。会黏包。要处理下。
        if md5_val == client_md5:
            conn.send(b'100')
        else:
            conn.send(b'10000')