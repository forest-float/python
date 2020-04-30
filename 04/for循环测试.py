#!/usr/bin/python3
# @Author: WLP
# @name: for循环测试.py
# @date 2020-04-29 14:03

import os
with open('1.txt', 'r') as f:
	for line in f.readlines():
		with open('2.txt', 'r') as f2:
			for line2 in f2.readlines():
				print(line.strip()+line2.strip())





