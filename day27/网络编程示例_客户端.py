# coding:utf-8

import socket

client = socket.socket()

# 向服务端发起连接请求(递伞)
# 阻塞，知道连接成功后才会继续向下走
client.connect(('127.0.0.1', 8000))


# 链接上服务端后，向服务端发送消息。
client.send(b'hello')

# 等待服务端回消息
data = client.recv(1024)
print(data)

client.close()
