#!/usr/bin/python3
# @Author: WLP
# @name: 迭代器和生成器.py
# @date 2020-04-27 16:58

# 迭代器是实现了迭代器协议的对象。#
# Python中没有像protocol或interface这样的定义协议的关键字。
# Python中用魔术方法表示协议。
# __iter__和__next__魔术方法就是迭代器协议。

class Fib(object):
    """迭代器"""

    def __init__(self, num):
        self.num = num
        self.a, self.b = 0, 1
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < self.num:
            self.a, self.b = self.b, self.a + self.b
            self.idx += 1
            return self.a
        raise StopIteration()


# 生成器是语法简化版的迭代器。

def fib(num):
    """生成器"""
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a + b
        yield a


# 生成器进化为协程。#
# 生成器对象可以使用send()
# 方法发送数据，发送的数据会成为生成器函数中通过yield表达式获得的值。
# 这样，生成器就可以作为协程使用，协程简单的说就是可以相互协作的子程序。

def calc_avg():
    """流式计算平均值"""
    total, counter = 0, 0
    avg_value = None
    while True:
        value = yield avg_value
        total, counter = total + value, counter + 1
        avg_value = total / counter


gen = calc_avg()
next(gen)
print(gen.send(10))
print(gen.send(20))
print(gen.send(30))




