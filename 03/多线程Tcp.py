#!/usr/bin/python3
# @Author: WLP
# @name: 多线程Tcp.py
# @date 2020-04-26 13:27

from socket import socket, SOCK_STREAM, AF_INET
from base64 import b64encode
from json import dumps
from threading import Thread


def main():
    # 自定义线程类
    class FileTransferHandler(Thread):

        def __init__(self, cclient):
            super().__init__()
            self.cclient = cclient

        def run(self):
            my_dict = {}
            my_dict['filename'] = 'guido.jpg'
            # JSON是纯文本不能携带二进制数据
            # 所以图片的二进制数据要处理成base64编码
            my_dict['filedata'] = data
            # 通过dumps函数将字典处理成JSON字符串
            json_str = dumps(my_dict)
            # 发送JSON字符串
            self.cclient.send(json_str.encode('utf-8'))
            self.cclient.close()

    # 1.创建套接字对象并指定使用哪种传输服务
    server = socket(family=AF_INET, type=SOCK_STREAM)
    # 2.绑定IP地址和端口(区分不同的服务)
    server.bind(('192.168.1.71', 5566))
    # 3.开启监听 - 监听客户端连接到服务器
    server.listen(512)
    print('服务器启动开始监听...')
    with open('guido.jpg', 'rb') as f:
        # 将二进制数据处理成base64再解码成字符串
        data = b64encode(f.read()).decode('utf-8')
    while True:
        client, addr = server.accept()
        # 启动一个线程来处理客户端的请求
        FileTransferHandler(client).start()


'''
我们使用了JSON作为数据传输的格式（通过JSON格式对传输的数据进行了序列化
和反序列化的操作），但是JSON并不能携带二进制数据，因此对图片的二进制数
据进行了Base64编码的处理。Base64是一种用64个字符表示所有二进制数据的编
码方式，通过将二进制数据每6位一组的方式重新组织，刚好可以使用0~9的数字、
大小写字母以及“+”和“/”总共64个字符表示从000000到111111的64种状态。
'''

if __name__ == '__main__':
    main()



