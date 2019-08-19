import socket
import requests
key_list = ['alex', 'db', 'john']

# 请求三个数据

#方式1
def get_data(key):
    client = socket.socket()

    client.connect(('www.baidu.com', 80))

    client.sendall(b'GET /s?wd=%s HTTP/1.0\r\nhost:www.baidu.com\r\n\r\n' %key)

    chunk_list = []

    while True:
        chunk = client.recv(8096)
        if not chunk:
            break
        chunk_list.append(chunk)

    body = b''.join(chunk_list)
    print(body.decode('utf-8'))


# for item in key_list:
#     get_data(item)

# 方式2
# for item in key_list:
#     ret = requests.get('https://www.baidu.com/s?Wd=%s' %item)


# 用多线程的方式解决
import threading

for item in key_list:
    t = threading.Thread(target=get_data, args=(item, ))
    t.start()

# 用单线程+IO不等待