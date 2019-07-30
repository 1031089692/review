# -*- coding: utf-8 -*-
import socket

# 未完待续


class Login:
    sk = socket.socket()
    sk.connect(('192.168.0.186', 8002))
    sk.listen(5)
    lst = {}
    conn, addr = sk.accept()
    count = 3

    def select(self):
        name = input('请选择1、登陆2、注册(请输入序号):')
        self.sk.send(name.encode('utf-8'))
        data = self.conn.recv(1024)
        if data == b'1':
            self.login()
        elif data == b'2':
            self.register()
        else:
            response = b'select error'
            self.conn.send(response)
            self.select()

    def register(self):
        try:
            input("请输入您需要注册的账号名：")
            user_data = self.conn.recv(1024)
            if user_data in self.lst.keys():
                data = '账号已存在，请勿重复注册'
                self.conn.send(data.encode())
            else:
                input("请输入您需要注册的账号名的密码：")
                pwd_data1 = self.conn.recv(1024)
                input("请再次输入您需要注册的账号名的密码：")
                pwd_data2 = self.conn.recv(1024)
                if pwd_data1 != pwd_data2:
                    response = "两次输入的密码不一致，请重试"
                    self.conn.send(response.encode())
                    self.register()
                else:
                    response = '注册成功'
                    self.conn.send(response.encode())
                    self.lst.update({'%s' % user_data: '%s' % pwd_data1})
                    self.select()
        except Exception as e:
            print(e)

    def login(self):
        try:
            while self.count > 1:
                input('请输入您的账号:')
                user_data = self.conn.recv(1024)
                if user_data in self.lst.keys():
                    input('请输入您的密码:')
                    pwd_data = self.conn.recv(1024)
                    if pwd_data in self.lst.values():
                        pwd_response = b'Login successfully'
                        self.conn.send(pwd_response)
                    else:
                        self.count -= 1
                        pwd_response = '密码错误请重试。您还可以输入%s次' % self.count
                        self.conn.send(pwd_response.encode())
                        continue
                else:
                    user_response = '对不起，,您的账号输入错误，请重试！'
                    self.conn.send(user_response.encode())
                    self.select()
                    break
            else:
                response = "对不起。您的账号已经连续输错三次。账号已锁定。请明天再试试"
                self.conn.send(response.encode())
        except Exception as e:
            print(e)


if __name__ == '__main__':
    a = Login()
    a.select()