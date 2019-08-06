# coding:utf-8
import socketserver
'''
在socketserver模块中
conn = self.request
'''


class Myserver(socketserver.BaseRequestHandler):

    def handle(self):
        '''
        这里写逻辑代码
        :return:
        '''
        pass


# 相当于 1、创建socket对象   2、self.socket.bing()  3、self.socket.listen(5)
server = socketserver.ThreadingTCPServer(('127.0.0.1', 8899), Myserver)

# 相当于执行server.accept(),返回两个参数。
server.serve_forever()
