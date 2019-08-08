# coding:utf-8
import os
import socket
import json
import hashlib

CODE = {
    '1001': '上传文件，从头开始上传'
}


def file_md5(file_path):
    """
    文件进行md5加密
    :param file_path:
    :return:
    """
    obj = open(file_path, 'rb')
    m = hashlib.md5()
    for line in obj:
        m.update(line)
    obj.close()
    return m.hexdigest()


sk = socket.socket()
sk.connect(('127.0.0.1', 8081))


while True:
    cmd = input("请输入要执行的命令:")
    if cmd == 'exit':
        break
    else:
        # 1、自定义协议
        file_path = "0.jpg"
        file_md5_val = file_md5(file_path)
        file_name = os.path.basename(file_path)
        file_size = os.stat(file_path).st_size

        cmd_dict = {'cmd': 'upload', 'file_name': file_name, 'size': file_size, 'md5': file_md5_val}
        upload_cmd_bytes = json.dumps(cmd_dict)
        upload_cmd_bytes = upload_cmd_bytes.encode('utf-8')
        sk.sendall(upload_cmd_bytes)

        # 2、等待服务端的响应
        response = json.loads(sk.recv(8096).decode('utf-8'))
        print(response)
        if response['code'] == 1001:
            f = open(file_path, mode='rb')
            send_size = 0
            while send_size < file_size:
                data = f.read(1024)
                sk.sendall(data)
                send_size += len(data)
            f.close()
            print('上传成功')
        else:
            # 续传---暂不考虑重复的情况
            exist_size = response['size']
            f = open(file_path, 'rb')
            f.seek(exist_size)  # 光标跳到上次传到的位置
            send_size = exist_size
            while send_size<file_size:
                data = f.read(1024)
                sk.sendall(data)
                send_size += len(data)
            f.close()
            print('上传成功')