# -*- coding: utf-8 -*-
# @Author: wlp
# @Date:   2020-04-23 09:43:58
# @Last Modified by:   forest-float
# @Last Modified time: 2020-04-26 11:16:37

from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime

def main():
	server = socket(family=AF_INET, type=SOCK_STREAM)
	server.bind(('192.168.1.71',6789))
	server.listen(512)
	print('服务器开启监听')
	while True: 		
		client,addr = server.accept()
		print(client.recv(1024).decode('utf-8'))
		client.send(str(datetime.now()).encode('utf-8'))
		print(str(addr) + '连接到了服务器.')
		client.send(str(datetime.now()).encode('utf-8'))
		client.close()
if __name__ == '__main__':
	main()
