# coding:utf-8


class BaseMessage(object):
    def send(self, x1):
        """
        必须继承BaseMessage,然后其中必须编写send方法，用于完成具体业务逻辑
        :param x1:
        :return:
        """
        raise NotImplementedError('.send()必须被重写')


class Email(BaseMessage):
    def send(self, x1):
        """
        必须继承BaseMessage,然后其中必须编写send方法，用于完成具体业务逻辑
        :param x1:
        :return:
        """
        pass


obj = Email()
obj.send(1)