# coding:utf-8
import socket


# 创建socket对象
server = socket.socket()

# 绑定IP和端口
server.bind(('192.168.0.186', 8000))

# 后面可以等5个人
server.listen(5)

# 等待客户端来连接，如果没人来就等待
# conn是客户端和服务端连接的对象（伞），服务端以后要通过该对象进行收发数据。
# addr是客户端的地址信息
conn, addr = server.accept()


# 通过对象去获取，(客户端通过伞发送的消息)
data = conn.recv(1024)
print(data)

# 服务端通过连接对象（伞）给客户端回复消息
conn.send(b'stop')

# 与客户端断开连接(放开伞)
conn.close()

# 关闭服务端的连接。
server.close()
