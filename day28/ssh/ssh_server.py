# coding:utf-8

import socket
import subprocess

server = socket.socket()
server.bind(('192.168.0.186', 8009))
server.listen(5)    # 设置连接数

while True:    # 循环实现多连接
    print("server is working......")
    conn, addr = server.accept()
    while True:   # 循环实现多次命令
        try:
            cmd = conn.recv(1024).decode('utf8')  # 阻塞,接收用户发送命令

            if cmd == b'exit':   # 退出
                break

            res = subprocess.Popen(       # Popen方法，可以将字符串转为命令
                cmd,
                shell=True,
                stderr=subprocess.PIPE,
                stdout=subprocess.PIPE,
            )
            out = res.stdout.read()   # 正常内容 类型是字节串
            err = res.stderr.read()   # 错误内容

            print("out响应长度", len(out))
            print("err响应长度", len(err))

            if err:
                import struct
                header_pack = struct.pack("i", len(err))  # i模式压缩。压缩后长度固定了
                conn.send(header_pack)     # 发送异常内容的包长度
                conn.send(err)             # 发送异常内容的包
            else:
                import struct
                header_pack = struct.pack("i", len(out))
                print("header_pack", header_pack)  # 打印包长
                conn.send(str(len(out)).encode('utf8'))  # 发送包长
                conn.send(out)   # 发送包

        except Exception as e:
            break
    conn.close()  # 关闭链接

# server.close()  # 关闭服务

