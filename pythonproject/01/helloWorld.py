
print('hello pathon')
print(type(123))
print(type(123.0))
print(type("123"))
print(type('123'))
print(isinstance(23, float))#判断前者是否是后者类型
print(1/3)#小数
print(type(1+2j))#复数,数学中为a+bi,python程序里面用j来代替i，原因是i在Python中不能表示虚数
print(1+1j)

print('hello world')
print("hello python")
print("i say: \"are you eat?\"")#出现在打印函数里面的双引号，如果要显示双引号，要添加转义字符\

print(len('I like Python!'))#len()获取字符串的长度

a = "Hello"
b = "Python"

print(a*2)#显示hellohello
print(a, '', b)#hello python
print(a, " ", b)#Hello   Python
# a   b 输出结果： Hello Python
print(a[1:3])#显示el  截取字符串  ，遵循左闭右开的原则

#成员运算符 in 可以判断一个字符串种是否包含指定的字符串，并返回 true 或者 false 布尔值。
if "o" in a:
    print('yes')
else:
    print('no')
#不包含
if "o" not in a:
    print('yes')
else:
    print('no')

print(123.5  + 123)
print(int(123.8+0.8))#强制类型转换是直接抹去小数
print(int(round(123.8+0.8)))#使用round函数实现四舍五入
print("a的内容为",a,"b的内容为",b)

print("11. -1 的绝对值为：", abs(-1))

print("12. 创建的复数为：", complex(1, -2))

print("13. 商和余数为：", divmod(10, 3))

print("14. 浮点型转换：", float(1))

print("15. 10的3次幂为：", pow(10, 3))

print("16. 四舍五入为：", round(5.5))

print("17. 集合求和结果为：", sum({1, 2, 3, 4}))

print("18. 整数20的二进制为：", bin(20))

print("19. 整数20的八进制为：", oct(20))

print("20. 整数20的十六进制为：", hex(20))

print("21. Unicode 为 97 的字符串：", chr(97))

print("22. 字符串 a 的 Unicode 码：", ord('a'))

print("23. 123 的 boolean 值为：", bool(123))

print("24. 空字符串的 boolean 的值为：", bool(''))

c=9
d=10
c **= d
print("c **= a 的值为：", c)
#**表示幂级数计算
c //= d
print("c //= a 的值为：", c)
#" / "  表示浮点数除法，返回浮点结果;     6/4=1.5
#" // " 表示整数除法,返回不大于结果的一个最大的整数  6//4=1

#逻辑运算符   与and     或or     非not
print(True and True)
# True
print(True and False)
# False
print(True or True)
# True
print(True or False)
# True
print(False or False)
# False
print(not True)
# False
print(not False)
# True

#成员运算符    in    not in


#身份运算符用于比较两个对象的存储单元。
#is ： is 是判断两个标识符是不是引用自一个对象
#is not ： is not 是判断两个标识符是不是引用自不同对象
c=d=10
if a is b:
    print("a 和 b 有相同的标识")
else:
    print("a 和 b 没有相同的标识")
if c is not d:
    print("c 和 d 没有相同的标识")
else:
    print("c 和 d 有相同的标识")
if id(c) == id(d):
    print("c 和 d 有相同的标识")
else:
    print("c 和 d 没有相同的标识")
d=11
if id(c) == id(d):
    print("c 和 d 有相同的标识")
else:
    print("c 和 d 没有相同的标识")
#id() 函数用于获取对象内存地址
#其实这个输出结果可以看出来，在 Python ，如果两个数值一样的变量，
# Python 并不会在内存中重新开辟内存空间，而是会复用已有的内存空间。
'''
weight = input("请输入当前的体重：")

if float(weight) >= 200:
    print("你和加菲猫一样肥！！")
else:
    print("你还是很苗条的么！！")
'''
i=10
while i >= 0:
    print("操作1")
    print("操作2")
    i-=1
    print("操作3")#到这里为止，都实在while循环里面，接下去的一条语句，因为没有缩进，表示在循环之外了
print("操作4")

for index in "Python":
    print(index)
#循环 “Python” 这个字符串里的每位字符

for index in range(5):
    print(index)
for index in range(0, 10, 3):
    print(index)
'''
range(start, stop[, step])

start：计数从 start 开始。
stop：计数到 stop 为止，但不包括 stop 。
step：步长，也叫间隔。
'''
#  break    continue


'''
多行注释    注释为三个单引号
多行注释
多行注释
'''
"""
多行注释    注释为三个双引号
多行注释
多行注释
"""

#列表
lista = []
list1 = [1, 2, 3, 4, 5, 6]
print(list1)
list2 = [1, 2, 3, 4, 5, 6, 'a', 'b', 'c']
print(list2)
list3 = [1, 2, 3, 4, 5, 6, 'a', 'b', 'c', list2]
print(list3)
print(type(list3))#类型就是列表list
#列表中的数据类型可以是相同的，如上面的 int 和 str ，也可以是不同的：
#列表里面是可以嵌套列表的
#Python 列表除了正索引还有一个负索引，正索引是列表从头到尾的方向，负索引的是从尾到头。
#列表:  ['a', 'b', 'c', 'd', 'e']
#         |    |    |    |    |
#正索引:  0    1    2    3    4
#负索引:  -5  -4   -3   -2   -1
print(list1+list2)#使用加号连接列表
for i in list1:#对列表元素进行 for 循环
    print(i)

print(len(list1))
print(len(list1+list2))#获取列表长度  len

print('a' in list1)#检查列表中是否存在某个元素    TRUE   FLASE
print(1 in list1)

print(min(list1))#列表中元素的最小值
print(max(list1))#列表中元素的最大值

print(list3[3:8])#列表的切片
print(list3[1:8:2])#列表的切片
del list1[1]#删除列表的第二个元素
del list1#删除列表，列表就保存在了
list3.append(1)#在列表末尾添加新的对象
print(list3)
print(list3.count(1))#统计某个元素在列表中出现的次数
lista.extend(list3)#在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
print(lista)
print(lista.index(1))#从列表中找出某个值第一个匹配项的索引位置
lista.insert(0,2)#将对象插入列表  index 是插入的索引值， obj 是要插入的元素。
print(lista)
list2.remove(4)#移除列表中某个值的第一个匹配项
print(list2)
list2.reverse()#反向列表
print(list2)

list3.pop()
print(list3)
list3.pop(1)
print(list3)#移除列表中的一个元素（默认最后一个元素），并且返回该元素的值

list4 = [2,4,6,3,1,5]
list4.sort()#列表的排序
print(list4)
list4.reverse()
print(list4)

#list.clear() （清空列表）

#元组    元组的元素不能修改
#元组使用小括号，列表使用方括号

tuple1 = "Python", "Java", 2011, 2015
print(tuple1)
#用逗号隔开的就是元组，但是为了美观和代码可读性，一般加小括号
tuple2 = ("Python", "Java", 2011, 2015)
print(tuple2)
print(type(tuple2))
#在创建元组的时候可以包含列表
tuple3 = ("Python", "Java", [1 , 2, 'python', 'java'], 2011, 2015)
print(tuple3)

tuple4 = (0 ,1, 2, 3, 4, 5, 6, 7, 8, 9)
print(tuple4)
# 索引
print(tuple4[2])
# 索引
print(tuple4[-2])
# 切片
print(tuple4[0:8:2])#遵循左闭右开原则
# 切片
print(tuple4[8:1:-1])
#切片
print(tuple4[0:6])

tuple5 = (2333, '98k')
# 连接
print(tuple4 +  tuple5)
# 循环
for index in tuple4:
    print(index)
# 查找元素是否存在
print(1 in tuple4)
print(11 in tuple4)
# 删除元组
# del tuple5
# print(tuple5)

# 取最大
print(max(tuple4))
# 取最小
print(min(tuple4))
# 元组长度
print(len(tuple4))
# 修改元组
#tuple4[0] = 11
#元组的数据是不可变的，修改数据会报错

#元组和列表相互转换
#在列表外套一层 tuple() 就可以转为元组
#在元组外套一层 list() 就可以转为列表

# 元组解包
tuple6 = (1, 2, 3)
print(tuple6)
a, b, c = tuple6
print(a, b, c)



#字典

dict1 = {"name1": "wlp", "age": 1}
print(dict1)
print(type(dict1))

dict2 = {(1, 2, 3): '123', 'name': 'geekdigging', 2: [1, 2, 3]}
print(dict2)
print(type(dict2))

#在使用‘=’去赋值的时候，键只能为字符串类型，并且创建的时候字符串不能加引号，加上就会直接报语法错误。
dict3 = dict(name =  'geekdigging', age = 2)
print(dict3)
print(type(dict3))

print(dict3['age'])#访问字典中的值

strs = 'geekdigging'
if strs in dict3:        #语法:  键  in  字典
    print(dict3['name'])
else:
    print('该键不存在字典中')
strs = 'name'
if strs in dict3:        #语法:  键  in  字典
    print(dict3['name'])
else:
    print('该键不存在字典中')


# 添加键
dict1['a'] = 18
print(dict1)
# 更新键
dict1['name'] = 'www.geekdigging.com'
print(dict1)
# 删除键
del dict1['a']
print(dict1)

print(dict1.keys())
#返回一个迭代器，可以使用 list() 来转换为列表，该列表包含所有的 key。
print(dict1.values())
#返回一个迭代器，可以使用 list() 来转换为列表，该列表包含所有的 value 。
print(list(dict1.keys()))#转为列表
print(tuple(dict1.keys()))#转为元组

print(dict1.items())#以列表返回可遍历的(键, 值) 元组数组
#dict_items([('name1', 'wlp'), ('age', 1), ('name', 'www.geekdigging.com')])
print(list(dict1.items()))
print(tuple(dict1.items()))

#返回指定键的值，如果值不在字典中返回 default(None) 值。
print(dict1.get('name'))
print(dict1.get('aaaaa'))#不存在该键的话返回None

#删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。
print(dict1.pop('age'))
print(dict1)

#和get()类似, 但如果键不存在于字典中，将会添加键并将值设为 default
print(dict1.setdefault('age'))
print(dict1)

#把字典 dict2 的键/值对更新到 dict 里。
dict2 = {'sex': 'male'}
dict1.update(dict2)
print(dict1)

#删除字典内所有元素。
dict2.clear()
print(dict2)

dict3 = {'name': 'geekdigging', 'age': [1, 2, 3]}
# 浅拷贝: 引用对象
dict4 = dict3
print(id(dict3))
print(id(dict4))
# 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用
dict5 = dict3.copy()
dict3['age'].remove(1)
print(dict3)
print(dict5)
print(id(dict3))
print(id(dict5))

#集合
#集合（set）是一个无序的不重复元素序列。
#{3, 2, 1} 和 {1, 2, 3} 是一样的。
#{1, 2, 2} 是不存在的，只会存在 {1, 2}。
#集合里的元素需要是不可变类型。   元组里面的数据也是不可变的

#创建一个空集合必须用 set() 而不是 {}，因为 {} 是用来创建一个空字典。
set3 = set()
print(set3)
# 演示集合不可变元素
set1 = {1, 2, 3, 'Python', (1, 'geekdigging')}
print(set1)
print(type(set1))
# 演示不可重复
set2 = {1, 2, 2}
print(set2)

# 使用 list 创建集合    消重功能
list1 = [1, 1, 2, 2, 3, 4]
set4 = set(list1)
print(set4)

#使用元组创建集合      消重功能
tuple1 = (1, 2, 3, 4, 3, 5, 6)
set5 = set(tuple1)
print(set5)

# 使用字符串创建集合    消重功能
str1 = 'geekdigging'
set6 = set(str1)
print(set6)

set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 7, 9}

# 求交集
set3 = set1.intersection(set2)
print('交集：', set3)

# 求并集
set4 = set1.union(set2)
print('并集：', set4)

# 做差
set5 = set1.difference(set2)
print('做差：', set5)
set1.add(7)
print(set1)
set7 = {1, 2}
set7.update({3, 4, 'python', (4, 5)})
print(set7)
#add里面的是一个参数，而update里面的是一个集合

set7.pop()#随机移除一个元素
print(set7)

set7.remove(3)#移除一个指定的元素，元素不存在则报错
print(set7)

set7.discard(3)#删除集合中指定的元素，元素不存在则什么都不做。
print(set7)

set7.clear()#清除集合中的所有元素，并不会清除集合
print(set7)

set10 = {1, 2, 3}
set11 = {1, 2}
set12 = {4, 5}
print(set10.isdisjoint(set11))#判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False
#false
print(set10.isdisjoint(set12))#true

#判断指定集合是否为该方法参数集合的子集
print(set11.issubset(set10))#判断指定集合set11,是不是set10方法参数的子集
print(set11.issubset(set12))

#判断该方法的参数集合是否为指定集合的子集
print(set10.issuperset(set11))#判断set11方法参数,是不是指定集合set10的子集
print(set11.issuperset(set12))

#函数
def add(a,b):
    c = a + b
    return c
c = add(1,2)
print(c)

def subtraction(a,b):
    return a-b
print(subtraction(b=5,a=10))#可以给形参变量赋值来进行非顺序参数输入

def division(a, b=1):
    return a / b
print(division(5))
print(division(10, 5))

def print_tuple(a, *b):#变长参数传递  元组
    print(a, b)

print(print_tuple(1,2,3,4,5,6,7,8))
print_tuple(1)#1 ()

def print_dict(a,**b):#边长参数传递   字典
    print(a,b)

print_dict(1, val = 2, key = 3, data = 'hellodict')
print_dict(1)#1 {}

#匿名函数
'''
当我们需要使用匿名函数的时候，可以使用 lambda 关键字来声明匿名函数。
lambda 只是一个表达式，函数体比 def 简单很多。
lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
语法：
函数对象名 = lambda 形参：表达式
'''
add = lambda x, y: x+y#匿名函数
print(add(1, 2))
max_num = lambda x, y: x if x >= y else y#匿名函数
print(max_num(5, 9))

def jieceng(i):#递归调用
    if i == 1:
        return 1
    else:
        return i * jieceng(i-1)
print('10的阶层为', jieceng(10))



#文件操作

'''
Python 为我们提供了打开文件的内置函数 open() 。
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
1
参数说明:

file: 必需，文件路径（相对或者绝对路径）。
mode: 可选，文件打开模式
buffering: 设置缓冲
encoding: 一般使用 utf-8
errors: 报错级别
newline: 区分换行符
closefd: 传入的file参数类型

模式	描述
t	文本模式 (默认)。
x	写模式，新建一个文件，如果该文件已存在则会报错。
b	二进制模式。
打开一个文件进行更新(可读可写)。
r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。
r	打开一个文件用于读写。文件指针将会放在文件的开头。
rb	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。一般用于非文本文件如图片等。
w	打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
w	打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb	以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
a	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。

'''
#str1 = open('F:/pythonproject/01/helloWorld.py', mode='r').read()
#出现错误UnicodeDecodeError: 'gbk' codec can't decode byte 0xad in position 181: illegal multibyte sequence
str1 = open('F:/pythonproject/01/helloWorld.py', mode='r',encoding= 'utf-8')
print(str1.read())
str1.close()

#在 Python3 中，文件默认的编码方式是 UTF-8 ，文本字符的常用的编码有 ASCII 和 Unicode 。
str2 = '好好学习，天天向上'
print(type(str2))
a = str2.encode('utf-8')
print(type(a))
print(a.decode('utf-8'))

#OS模块
import os
import shutil
os.chdir('F:/pythonproject/01/')#导入路径
#w	打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，
# 即原有内容会被删除。如果该文件不存在，创建新文件。
file = open('test.txt', mode='a', encoding='utf-8')#如果该文件已存在，
# 文件指针将会放在文件的结尾,不存在则创建
file.write('你好，python!')
try:
    print(file.read())
except:
    print('读取文件异常')
    file.close()
    file = open('test.txt', mode='r', encoding='utf-8')#以只读方式打开文件。文件的指针将会放在文件的开头
    print(file.read())
finally:
    file.close()
try:
    #os.renames('test.xlsx','test1.xlsx')   #更改文件名字
    shutil.copyfile('test.xlsx','test1.xlsx')#复制文件
except FileNotFoundError:
    os.renames('test1.xlsx', 'test.xlsx')
#shutil.copyfile(old_name, new_name)

#在代码中打印了两次，为什么只显示了一次呢
#read() 读取所有内容，读取完后，游标是指在最后的，再往后读取肯定就读不到内容了


#基础异常处理
'''
try:
    ...(可能产生异常的代码)
except:
    ...(产生异常后的处理代码)
finally:
    ...(一定要执行的代码)
'''
def division(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print('程序出现异常zero')
        return None
    except TypeError:
        print('参数类型错误')
        return None
    except:
        print('程序出现异常')
        return None
    finally:
        print('你一定能看到我！！！')

print(division(15, 3))
print(division(15, 0))
print(division(15, a))

#迭代器
'''
迭代器可以简单的理解为 for 循环， Python 除了 for 循环为我们准备了另一种访问集合元素的方式。
特点：
可以记住遍历的位置的对象。
迭代器从集合的第一个元素开始访问，直到所有的元素访问结束。
迭代器只能向前不能后退。
但是判断一个对象是否有迭代器，除了看它能不能使用 for 循环外， Python 也为我们提供了更加专业的方法—— isinstance() 。

我们可以使用 isinstance() 来判断当前的对象是否可以迭代。
在使用迭代器之前，需要先将迭代器引入，因为迭代器不是 Python 的内置方法
'''
from collections.abc import Iterable    #引入迭代器，迭代器不是python的内置方法

print(isinstance('geekdigging', Iterable))
print(isinstance([], Iterable))
print(isinstance([], Iterable))
print(isinstance({x for x in range(5)}, Iterable))
print(isinstance(123, Iterable))

#列表并不是一个迭代器。所以，可迭代对象不一定是迭代器！
list1 = [1, 2, 3, 4]
try:
    next(list1)
except TypeError:
    list1 = iter(list1)#我们导入 Iterator 模块，先将列表转换成迭代器，
    print(next(list1))
finally:
    print('下一个 next')
print(next(list1))
print(next(list1))
print(next(list1))
try:
    print(next(list1))
except StopIteration:
    print('列表已结束')

#生成器
list1 = [x*x for x in range(10)]
print(list1)
#生成一个列表   但是如果范围的值很大比如100000000000000，，那么系统就会奔溃
#报错信息提示我们存储异常，并且整个程序运行了相当长一段时间

generator1 = (x*x for x in range(1000000000000000000000000))#生成器
print(generator1)
print(type(generator1))

generator3 = (x*x for x in range(5))
for index in generator3:
    print(index)
#generator 非常的强大，本质上， generator 并不会取存储我们的具体元素，
# 它存储是推算的算法，通过算法来推算出下一个值。

def print_a(max):
    i = 0
    while i < max:
        i  = i+1
        yield i
#这里使用到了关键字 yield ， yield 和 return 非常的相似，都可以返回值，
# 但是不同的是 yield 不会结束函数。
a = print_a(10)#创建了一个生成器
print(a)
print(type(a))
#我们调用几次这个用函数创建的生成器：
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(a.__next__())#相当于next(a)
print(a.__next__())
print(a.__next__())
'''
可以看到，当我们使用 next() 对生成器进行一次操作的时候，会返回一次循环的值，
在 yield 这里结束本次的运行。但是在下一次执行 next() 的时候，
会接着上次的断点接着运行。直到下一个 yield ，并且不停的循环往复，
直到运行至生成器的最后。
'''
def print_b(max):
    i = 0
    while i < max:
        i  = 1
        args = yield i
        print('传入参数为：', args)

b = print_b(20)
print(next(b))
print(b.send('Python'))#还能给函数再传一个值回去：

def print_c():
    while True:
        print('执行 A ')
        yield None
def print_d():
    while True:
        print('执行 B ')
        yield None
#生成器可以用作进行协程操作，相当于多线程
c = print_c()
d = print_d()
for i in range(1, 10, 3):
    c.__next__()
    d.__next__()

#time时间模块
import time
for i in range(3):
    print('sleep 1 s')
    time.sleep(1)
print(time.localtime())
print(time.mktime(time.localtime()))#将本地时间转换成一个时间戳
print(time.asctime(time.localtime()))#将本地时间转换成时间格式显示
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))#将英文时间格式转换成中文显示
'''
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
'''


#calendar模块   日历
import calendar

#w = 每个日期之间的间隔字符数  l = 每周所占用的行数  c = 每个月之间的间隔字符数
print(calendar.calendar(theyear=2020, w=1, l=1, c=4))#显示全年的日历

print(calendar.month(2020, 1))#显示某月的日历
print(calendar._monthlen(2020, 2))#计算某一个月的天数
print(calendar.weekday(2020, 1, 21))#显示指定日期是星期几


#excel表格操作 读取表格数据
'''
首先，我们需要导入第三方模块 xlrd ，因为是第三方的模块，没有安装的需要先安装。在命令行中输入：
pip install xlrd
'''

import xlrd
import xlwt
import datetime
# 打开execl
filename = '你好.txt'
filename = filename.encode('utf-8')#如果文件名有包含中文，使用编码格式转换

workbook = xlrd.open_workbook('test.xlsx')


# 输出所有 sheet 的名字
print(workbook.sheet_names())
# 获取所有的 sheet
print(workbook.sheets())
# 根据索引获取 sheet
print(workbook.sheet_by_index(1))
# 根据名字获取 sheet
print(workbook.sheet_by_name('1班'))

sheet1 = workbook.sheets()[0]
# 获取行数
print(sheet1.nrows)
# 获取列数
print(sheet1.ncols)

# 获取第 2 行内容
print(sheet1.row_values(1))
# 获取第 3 列内容
print(sheet1.col_values(2))

cell1 = sheet1.cell(1, 1).value
# 行索引
cell2 = sheet1.row(1)[1].value     #第二行第二列    row / col  行在前，列在后
cell3 = sheet1.cell(1, 2).value    #第二行第三列    cell行在前，列在后
# 列索引
cell4 = sheet1.col(2)[1].value     #第二行第三列
print(cell1, cell2, cell3, cell4)

#获取的是表格里面的时间数据
date_value = xlrd.xldate_as_datetime(sheet1.cell_value(5, 4),
                                     workbook.datemode)
print(type(date_value), date_value)
#这里是直接通过方法将数据转成了 datetime 类型，
# xlrd 还提供了可以将数据转成元组，然后再将元组转成日期。
date_value = xlrd.xldate_as_tuple(sheet1.cell_value(5, 4), workbook.datemode)
print(type(date_value), date_value)#元组类型
year, month, day, hours, minu, secon = date_value#将元组数据一一赋值给特定的变量
print(datetime.datetime(year, month, day, hours, minu, secon))#转换成时间格式



#写入 Excel    具体说明请看文档https://xlsxwriter.readthedocs.io/
#首先当然是安装第三方模块：
#pip install xlsxwriter

import xlsxwriter

workbook = xlsxwriter.Workbook('demo.xlsx')

sheet1 = workbook.add_worksheet('test_sheet')
sheet2 = workbook.add_worksheet('test2_sheet')

workfomat = workbook.add_format()
# 字体加粗
workfomat.set_bold(True)
# 单元格边框宽度
workfomat.set_border(1)
# 对齐方式
workfomat.set_align('left')
# 格式化数据格式为小数点后两位
workfomat.set_num_format('0.00')

heads = ['', '语文', '数学', '英语']
datas = [
    ['小明', 76, 85, 95],
    ['小红', 85, 58, 92],
    ['小王', 98, 96, 91]
]

#sheet1.write_row('A1', heads, workfomat)
sheet1.write_row(0, 0, heads, workfomat)
sheet1.write_row('A2', datas[0], workfomat)
sheet1.write_row('A3', datas[1], workfomat)
sheet1.write_row('A4', datas[2], workfomat)

format1 = workbook.add_format({'num_format': 'YYYY/mm/dd/ hh:mm:ss'})
sheet1.write_datetime('E6', datetime.datetime(2020, 1, 17, 13, 15, 16), format1)
'''
# 字符串类型
sheet1.write_string()
# 数字型
sheet1.wirte_number()
# 空类型
sheet1.write_blank()
# 公式
sheet1.write_formula()
# 布尔型
sheet1.write_boolean()
# 超链接
sheet1.write_url()

'''
sheet1.insert_image('I6', 'wx.jpg')#添加显示图片
''''
insert_image(row, col, image[, options])
row：行坐标，起始索引值为0；
col：列坐标，起始索引值为0；
image：string类型，是图片路径；
options：dict类型，是可选参数，用于指定图片位置，如URL等信息；
'''

chart = workbook.add_chart({'type': 'bar'})
'''
创建的图表的样式
area：面积样式的图表
bar：条形图
column：柱状图
line：线条样式的图表
pie：饼形图
scatter：散点图
stock：股票样式的图表
radar：雷达样式的图表
'''
chart.add_series({'values': '=test_sheet!$B$2:$D$2'})
chart.add_series({'values': '=test_sheet!$B$3:$D$3'})
chart.add_series({'values': '=test_sheet!$B$4:$D$4'})

#chart.add_series({'values': '=test_sheet!$E$2:$E$4'})
sheet1.insert_chart('A7', chart)#插入图表


workbook.close()#关闭Workbook


workbook = xlsxwriter.Workbook('chart_line.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': 1})

# Add the worksheet data that the charts will refer to.
headings = ['Number', 'Batch 1', 'Batch 2']
data = [
    [2, 3, 4, 5, 6, 7],
    [10, 40, 50, 20, 10, 50],
    [30, 60, 70, 50, 40, 30],
]

worksheet.write_row('A1', headings, bold)#写入行
worksheet.write_column('A2', data[0])#写入列
worksheet.write_column('B2', data[1])
worksheet.write_column('C2', data[2])

# Create a new chart object. In this case an embedded chart.
chart1 = workbook.add_chart({'type': 'line'})#line：线条样式的图表

# Configure the first series.
chart1.add_series({
    'name':       '=Sheet1!$B$1',#数据的名称
    'categories': '=Sheet1!$A$2:$A$7',#类别
    'values':     '=Sheet1!$B$2:$B$7',#值
})

# Configure second series. Note use of alternative syntax to define ranges.
chart1.add_series({
    'name':       ['Sheet1', 0, 2],
    'categories': ['Sheet1', 1, 0, 6, 0],#表示起始行，起始列，结束行，结束列
    'values':     ['Sheet1', 1, 2, 6, 2],#相当于‘=sheet1!$C$2:$C$7’
})

# Add a chart title and some axis labels.
chart1.set_title ({'name': 'Results of sample analysis'})#设置图表标题
chart1.set_x_axis({'name': 'Test number'})#设置x轴说明
chart1.set_y_axis({'name': 'Sample length (mm)'})#设置y轴说明

# Set an Excel chart style. Colors with white outline and shadow.
chart1.set_style(10)

# Insert the chart into the worksheet (with an offset).
worksheet.insert_chart('D2', chart1, {'x_offset': 25, 'y_offset': 10})#带有偏移量
workbook.close()


#批处理文件
import os
import shutil

file_names = os.listdir("./")
print(file_names)
try:
    os.mkdir("section1")
    os.mkdir("section2")
    os.mkdir("section3")
except FileExistsError:
    print('文件夹已经存在')
i = 0
for file_name in file_names:
    splited_file_name = file_name.split('.')
    print(splited_file_name)
    if  splited_file_name[0] == 'idea' \
            or 'section' in splited_file_name[0] \
            or splited_file_name[1] != 'bmp'  :
        continue
    #file_id = int(splited_file_name[0])
    #size_folder = "section"+str((file_id-1)%3+1)
    #shutil.move(file_name, os.path.join(os.getcwd(), file_name))

    os.renames(file_name, str(i)+'.png')#更改名字
    shutil.copyfile(str(i)+'.png', file_name)  # 复制文件

#move(src, dst)： 将src移动至dst目录下。若dst目录不存在，则效果等同于src改名为dst。
#若dst目录存在，将会把src文件夹的所有内容移动至该目录下面
#os.path.join()函数用于路径拼接文件路径。
#os.path.join()函数中可以传入多个路径：
#会从第一个以”/”开头的参数开始拼接，之前的参数全部丢弃。
#以上一种情况为先。在上一种情况确保情况下，若出现”./”开头的参数，
# 会从”./”开头的参数的上一个参数开始拼接。
#使用os.getcwd()函数获得当前的路径。




