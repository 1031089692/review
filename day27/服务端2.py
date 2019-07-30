# coding:utf-8
import socket

server = socket.socket()

server.bind(('192.168.0.186', 8001))

server.listen(5)


while True:
    conn, addr = server.accept()
    while True:
        data = conn.recv(1024)
        print(data)
        b = '刘强'.encode()
        if data == b'%s' % b:
            break
        response = data + b' sb'
        conn.send(response)
    conn.close()
    server.close()

