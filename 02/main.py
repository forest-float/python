
s = 'hello, this is python'

#输入和输出
print(str(s))#str()函数返回一个用户易读的表达形式  hello, this is python

print(repr(s))#repr()函数产生一个解释器易读的形式  'hello, this is python'

for i in range(1, 11):
    print(str(i).rjust(2), str(i**2).rjust(3), end=" ")
    print(str(i**3).rjust(4))
#九九乘法表
#字符串对象的 rjust() 方法, 它可以将字符串靠右, 并在左边填充空格。ljust() 和 center()
for i in range(1,10):
    for j in range(1, i+1):
        print(j, "*", i, "=", str(i*j).rjust(2), end="   ")
    print("")

for i in range(1,10):
    for j in range(1, i+1):
        print(j, "*", i, "=", str(i*j).zfill(3), end="   ")
    print("")

print(bin(20))#二进制
print(oct(20))#八进制
print(hex(20))#十六进制

#str.formate()函数格式化字段     位置和参数任意混合
print("value is {},to {}".format("hello", "python"))
print("value is {aaa},to {bbb}".format(aaa="hello", bbb="python"))#参数
print("value is {0},to {1}".format("hello", "python"))#位置
print("value is {1},to {0}".format("hello", "python"))
import math
print("pi value is {}".format(math.pi))
print("pi value is {0:.5f}".format(math.pi))
print("pi value is {0:.5f}".format(123456))#限制输出的位数
#老式字符串格式化  %   终将被str.formate()替代
print('The value of PI is approximately %5.3f.' % math.pi)


table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print('{0:10} ==> {1:10d}'.format(name, phone))
    #:后面加数值标志至少占多少宽度
#用[]来访问键值
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
          'Dcab: {0[Dcab]:d}'.format(table))
#用**来表示与用[]来表示
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))


import os
f = open("write.txt", "w")
f.write("this is first line.\n")
f.write("this is second line.\n")
f.close()

f = open("write.txt", "rb+")
s = f.read()
print(s, type(s))

s = f.tell()#返回当前位置
print(s, type(s))
'''
seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
seek(x,1) ： 表示从当前位置往后移动x个字符
seek(-x,2)：表示从文件的结尾往前移动x个字符
默认为0
'''
f.seek(-10, 2)
print(s, type(s))

s = f.readlines()
print(s, type(s))

# 写文件
with open("test.txt", "wt") as out_file:
    out_file.write("该文本会写入到文件中\n看到我了吧！")

# Read a file
with open("test.txt", "rt") as in_file:
    text = in_file.read()

#使用pickle模块将数据对象保存到文件

import pickle

data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open('data.pkl', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data1, output)

# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)

output.close()


#使用pickle模块从文件中重构python对象

import pprint, pickle

pkl_file = open('data.pkl', 'rb')

data3 = pickle.load(pkl_file)
print(data3)
pprint.pprint(data3)

data2 = pickle.load(pkl_file)
pprint.pprint(data2)

pkl_file.close()

class people:

    name = ' '
    age = 0
    __weight = 0

    def __init__(self, n, a, m):
        self.name = n
        self.age = a
        self.__weight = m

    def speak(self):
        print("name is {}, age is {}, __weight is {}"
              .format(self.name, self.age, self.__weight))


p = people(3, 5, 7)
p.speak()

#多重继承  class student(people1，people2):
#单继承
class student(people):
    grade = ''

    def __init__(self, n, a, m, g):
        people.__init__(self, n, a, m)
        self.grade = g

    #覆盖父类的写法
    def speak(self):
        print("grade is {}".format(self.grade))


#应用实例
s = student(1, 2, 3, 4)
s.speak()
print(s.name)
#两个下划线开头，声明该方法为私有方法，不能在类地外部调用。只能在类的内部调


#运算符重载

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):

        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)
'''
__init__ : 构造函数，在生成对象时调用
__del__ : 析构函数，释放对象时使用
__repr__ : 打印，转换
__setitem__ : 按照索引赋值
__getitem__: 按照索引获取值
__len__: 获得长度
__cmp__: 比较运算
__call__: 函数调用
__add__: 加运算
__sub__: 减运算
__mul__: 乘运算
__div__: 除运算
__mod__: 求余运算
__pow__: 乘方
'''

import os, shutil, glob

os.getcwd()      # 返回当前的工作目录

shutil.copyfile('main.py', 'main1.py')

glob.glob('*.py')#glob模块提供了一个函数用于从目录通配符搜索中生成文件列表:

import sys
#通用工具脚本经常调用命令行参数。这些命令行参数以链表形式存储于 sys 模块的 argv 变量
print(sys.argv)

#显示警告信息 大多脚本的定向终止都使用 "sys.exit()"。
#sys.stderr.write('Warning, log file not found starting a new one\n')
# sys.exit()
# x = input("x:")
# print(x)

print('tea for too'.replace('too', 'two'))

import re

print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))

import math

math.cos(math.pi / 4)

math.log(1024, 2)

import random

random.choice(['apple', 'pear', 'banana'])
random.sample(range(100), 10)   # sampling without replacement
random.random()    # random float
random.randrange(6)  # random integer chosen from range(6)

from urllib.request import urlopen

# for line in urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
#     line = line.decode('utf-8')  # Decoding the binary data to text.
#     if 'EST' in line or 'EDT' in line:  # look for Eastern Time
#         print(line)
#

#calendar模块   日历
import calendar

#w = 每个日期之间的间隔字符数  l = 每周所占用的行数  c = 每个月之间的间隔字符数
print(calendar.calendar(theyear=2020, w=1, l=1, c=4))#显示全年的日历

print(calendar.month(2020, 1))#显示某月的日历
print(calendar._monthlen(2020, 3))#计算某一个月的天数
print(calendar.weekday(2020, 3, 27))#显示指定日期是星期几

#time时间模块
import time
for i in range(3):
    print('sleep 1 s')
    time.sleep(1)
print(time.localtime())
print(time.mktime(time.localtime()))#将本地时间转换成一个时间戳
print(time.asctime(time.localtime()))#将本地时间转换成时间格式显示
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))#将英文时间格式转换成中文显示

#以下模块直接支持通用的数据打包和压缩格式：zlib，gzip，bz2，zipfile，以及 tarfile
import zlib
s = b'witch which has which witches wrist watch'
len(s)
t = zlib.compress(s)
len(t)
zlib.decompress(t)
zlib.crc32(s)


def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # 自动验证嵌入测试
#强化了文档，允许 doctest 模块确认代码的结果是否与文档一致:

import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        self.assertRaises(ZeroDivisionError, average, [])
        self.assertRaises(TypeError, average, 20, 30, 70)

unittest.main() # Calling from the command line invokes all tests
#可以在一个独立的文件里提供一个更全面的测试集
