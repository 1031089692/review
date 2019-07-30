# coding:utf-8
import subprocess


res = subprocess.Popen("ls",
                       shell=True,
                       stderr=subprocess.PIPE,
                       stdout=subprocess.PIPE)


print(res.stdout.read().decode('utf8'))
