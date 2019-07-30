# coding:utf-8

import socket

sk = socket.socket()
conn, addr = sk.accept()

sk.connect(('192.168.0.186', 8001))

while True:
    # name = input('请输入姓名：')
    # sk.send(name.encode('utf-8'))
    # if name == 'exit':
    #     break
    # response = sk.recv(1024)
    # print(response.decode('utf-8'))
    data = conn.recv(1024)
