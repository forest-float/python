# -*- coding: utf-8 -*-
# @Author: wlp
# @Date:   2020-04-02 17:11:08
# @Last Modified by:   forest-float
# @Last Modified time: 2020-04-08 14:18:30



arr = [3,5,2,7,3,8,1,2,4,8,9,3]

unique = set(arr)#获取非重复集合

a = map(arr.count,unique)#映射函数找出每个元素出现的次数，返回值是一个迭代器，但不能直接显示信息
b = list(a)
print(b)

c = zip(unique,b)#用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，
#然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。
d = list(c)
g = list(c)
print(d)
print(g)
# filter() 函数用于过滤序列，过滤掉不符合条件的元素，
# 返回一个迭代器对象，如果要转换为列表，可以使用 list() 来转换。
# 该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，
# 然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
e = filter(lambda x:x[0] == x[1],d)
f = list(e)
print(f)

print("幸运数是：",[item[0] for item in f])
print("幸运数是：",[item[0] for item in filter(lambda x:x[0] == x[1],(zip(unique,(map(arr.count,(set(arr)))))))])

