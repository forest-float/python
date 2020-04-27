#!/usr/bin/python3
# @Author: WLP
# @name: 客户端.py
# @date 2020-04-26 10:44

from socket import socket
import time
from datetime import datetime
# 客户端
def main():
    client = socket()
    client.connect(('192.168.1.71',6789))
    client.send(str(datetime.now()).encode('utf-8'))
    print(client.recv(1024).decode('utf-8'))
    client.close()
    time.sleep(1)


if __name__ == '__main__':
    while True:
        main()




