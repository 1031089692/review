import socket

client = socket.socket()
client.setblocking(False)   # 将原来阻塞的位置变成非阻塞(报错)

try:
    client.connect(('www.baidu.com', 80))   # 捕获这个错误
except:
    pass

client.sendall(b'GET /s?wd=alex HTTP/1.0\r\nhost:www.baidu.com\r\n\r\n' )

chunk_list = []
while True:
    chunk = client.recv(8096)  # 将原来阻塞的位置变成非阻塞(报错)
    if not chunk:
        break
    chunk_list.append(chunk)

body = b''.join(chunk_list)
print(body.decode('utf-8'))