import socket
import select

client1 = socket.socket()
client1.setblocking(False)
try:
    client1.connect(('www.baidu.com', 80))
except BlockingIOError as e:
    pass

client2 = socket.socket()
client2.setblocking(False)
try:
    client2.connect(('www.sougou.com', 80))
except BlockingIOError as e:
    pass

client3 = socket.socket()
client3.setblocking(False)
try:
    client3.connect(('so.m.sm.cn', 80))
except BlockingIOError as e:
    pass

socket_list = [client1, client2, client3]
conn_list = [client1, client2, client3]
while True:
    rlist,wlist,elist = select.select(socket_list, conn_list, [], 0.005)
    '''
    一共四个参数。
    第一个参数。socket_list，检测服务端是否返回数据---可读
    第二个参数。conn_list，检测其中的socket是否已经和服务端连接成功---可写
    第三个参数。[]，用来检测异常
    第四个参数。每次检测时间间隔
    '''
    for sk in wlist:
        if sk == client1:
            sk.sendall(b'GET /s?wd=alex HTTP/1.0\r\nhost:www.baidu.com\r\n\r\n')
        elif sk == client2:
            sk.sendall(b'GET /web?query=alex HTTP/1.0\r\nhost:www.sogou.com\r\n\r\n')
        else:
            sk.sendall(b'GET /s?q=alex HTTP/1.0\r\nhost:so.m.sm.cn\r\n\r\n')
        conn_list.remove(sk)

    for sk in rlist:
        chunk_list = []
        while True:
            try:
                chunk = sk.recv(8096)
                if not chunk:
                    break
                chunk_list.append(chunk)
            except BlockingIOError as e:
                break
        body = b''.join(chunk_list)
        print('-------->', body)
        #print(body.decode('utf-8'))
        sk.close()
        socket_list.remove(sk)

    if not socket_list:
        break
