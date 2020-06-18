#!/usr/bin/python3
# @Author: WLP
# @name: map&&filter&&reduce.py
# @date 2020-05-07 16:54

li = [12, 23, 34]
newli = list(map(lambda a: a+1, li))#遍历函数map
print(newli)
newli = list(filter(lambda x: x > 23, newli))#筛选函数filter
print(newli)
from functools import reduce
li = [11, 22, 33, 44]
newli = reduce(lambda arg1, arg2: arg1 + arg2, li, 100)
#第一个参数必须是有两个参数的函数
# 第二个参数是要循环的列表，
# 第三个参数是初始值，如果没有就是默认初始值为0
print(newli)
print(sum(li))

print(ord('a'))
print(chr(97))
s = 'I have a apple!'
lists = s.split(' ')#分割
print(lists)
ss = ''
ss = ss.join(lists)#逆分割
print(ss)

file = "F://adfaffjkjl.xls"
file.endswith('xls')#判断file是否以xls结尾
file.startswith("F://")#判断判断是否以F://开头
#s.replace(被查找词，替换词)
#re.sub(被替换词，替换词，替换域， flags=re.IGNORECASE)忽略大小写

'''
try
except
finally
'''

#关于Python中的数据备份问题

a = [1, 2, 3, 4]
c = a
#c是a的备份，但是备份失败，地址一样
print(id(a), id(c))
b = a[:]
#这样备份成功
print(id(a), id(b))
d = a.copy()
#也可以这样
print(id(a), id(d))


