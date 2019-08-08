# coding:utf-8
import socketserver
import struct
import os
import sys
import json
'''
在socketserver模块中
conn = self.request
'''


def eachfile(filepath):    # /Users/liuqiang/PycharmProjects/review/day30/TFP_WORK/server
    case = []
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        # child = os.path.join('%s%s' % (filepath, allDir))
        case.append(allDir)
    return case


class Myserver(socketserver.BaseRequestHandler):

    def handle(self):
        # 接收json的打包长度
        file_info_lenght_pack = self.request.recv(4)
        file_info_lenght = struct.unpack('i', file_info_lenght_pack)[0]

        # 接收json字符串
        file_info_json = self.request.recv(file_info_lenght).decode('utf8')
        file_info = json.loads(file_info_json)

        action = file_info.get('action')
        filename = file_info.get('filename')
        filesize = file_info.get('filesize')
        result = eachfile('/Users/liuqiang/PycharmProjects/review/day30/TFP_WORK/server')
        print(result)
        # 这里要增加判断逻辑，判断当前路径下是否已有需要接收的数据。
        if filename in result:
            print(1)
        else:
            print(2)


if __name__ == '__main__':
    # eachFile('/Users/liuqiang/PycharmProjects/review/day30/TFP_WORK/server')
    HOST, PORT = "localhost", 9999
    server = socketserver.ThreadingTCPServer((HOST, PORT), Myserver)
    server.serve_forever()

