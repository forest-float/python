#!/usr/bin/python3
#@Author: WLP
#@name: 正则表达式.py
#@date 2020-03-27 16:09

import re
print(re.match('www', 'www.w3cschool.cn').span())  # 在起始位置匹配
print(re.match('cn', 'www.w3cschool.cn'))         # 不在起始位置匹配
#re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。


line = "Cats are smarter than dogs"

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
else:
   print ("No match!!")


#re.search 扫描整个字符串并返回第一个成功的匹配。
print(re.search('www', 'www.w3cschool.cn').span())  # 在起始位置匹配
print(re.search('cn', 'www.w3cschool.cn').span())         # 不在起始位置匹配


line = "Cats are smarter than dogs"

searchObj = re.search(r'(.*) are (.*) .*', line, re.M | re.I)

if searchObj:
   print("searchObj.group() : ", searchObj.group())
   print("searchObj.group(1) : ", searchObj.group(1))
   print("searchObj.group(2) : ", searchObj.group(2))
else:
   print("Nothing found!!")

phone = "2004-959-559 # 这是一个电话号码"

abc = re.search(r'.*[0-9].', phone)
print("searchObj.group() : ", abc.group())#2004-959-559

# 删除注释
num = re.sub(r'#.*$', "", phone)
print ("电话号码 : ", num)

# 移除非数字的内容
num = re.sub(r'\D', "", phone)
print ("电话号码 : ", num)

