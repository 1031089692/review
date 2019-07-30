# coding:utf-8
import logging

logger = logging.basicConfig(filename='xx.text',
                             format='%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s',
                             datefmt='%Y-%m-%d %H:%M:%S',
                             level=30)

def func():
    try:
        a = a + 1
    except Exception as  e:
        logging.error(e)


func()