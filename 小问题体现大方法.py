# -*- coding: utf-8 -*-
# @Author: wlp
# @Date:   2020-04-02 17:11:08
# @Last Modified by:   forest-float
# @Last Modified time: 2020-04-03 09:35:52



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

e = filter(lambda x:x[0] == x[1],d)
f = list(e)
print(f)

print("幸运数是：",[item[0] for item in f])
print("幸运数是：",[item[0] for item in filter(lambda x:x[0] == x[1],(zip(unique,(map(arr.count,(set(arr)))))))])

