# coding:utf-8
import socketserver
import struct
import os
import sys
import json
import shutil


class NBServer(socketserver.BaseRequestHandler):
    def handle(self):
        """
        self.request 是客户端的socket对象
        :return:
        """
        # 1、接收命令
        upload_cmd_bytes = self.request.recv(8096)
        cmd_dict = json.loads(upload_cmd_bytes.decode('utf-8'))
        print(cmd_dict)

        # 2、获取文件信息
        file_md5 = cmd_dict['md5']
        file_name = cmd_dict['file_name']

        file_md5_path = os.path.join('home', file_md5)
        file_name_path = os.path.join('home', file_name)
        upload_file_size = cmd_dict['size']

        # 3、判断文件是否存在
        exist = os.path.exists(file_md5_path)
        print(exist)
        if not exist:  # 不续传
            # 3.1.1 返回状态码
            response = {'code': 1001}
            self.request.sendall(json.dumps(response).encode('utf-8'))

            # 3.1.2接收长传的文件内容
            f = open(file_md5_path, 'wb')
            recv_size = 0
            while recv_size < upload_file_size:
                data = self.request.recv(1024)
                f.write(data)    # 存入内存
                f.flush()    # 存入硬盘
                recv_size += len(data)
            f.close()

            # 3.1.3 改名字
            shutil.move(file_md5_path, file_name_path)
        else:
            # 断点续传
            exist_size = os.stat(file_md5_path).st_size
            response = {'code': 1002, 'size': exist_size}
            a = self.request.sendall(json.dumps(response).encode('utf-8)'))
            print(a)
            f = open(file_md5_path, 'ab')   # 这里要换成ab追加模式
            recv_size = exist_size
            while recv_size < upload_file_size:
                data = self.request.recv(1024)
                f.write(data)    # 存入内存
                f.flush()    # 存入硬盘
                recv_size += len(data)
            f.close()
            shutil.move(file_md5_path, file_name_path)


if __name__ == '__main__':
    HOST, PORT = "localhost", 8081
    server = socketserver.ThreadingTCPServer((HOST, PORT), NBServer)
    server.serve_forever()
