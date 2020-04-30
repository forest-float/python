#!/usr/bin/python3
# @Author: WLP
# @name: 并发编程.py
# @date 2020-04-27 17:00

# Python中实现并发编程的三种方案：多线程、多进程和异步I/O。
# 并发编程的好处在于可以提升程序的执行效率以及改善用户体验；
# 坏处在于并发的程序不容易开发和调试，同时对其他程序来说它并不友好。

'''
多线程：Python中提供了Thread类并辅以Lock、Condition、Event、
Semaphore和Barrier。Python中有GIL来防止多个线程同时执行本地
字节码，这个锁对于CPython是必须的，因为CPython的内存管理并不
是线程安全的，因为GIL的存在多线程并不能发挥CPU的多核特性。
'''

"""
面试题：进程和线程的区别和联系？
进程 - 操作系统分配内存的基本单位 - 一个进程可以包含一个或多个线程
线程 - 操作系统分配CPU的基本单位
并发编程（concurrent programming）
1. 提升执行性能 - 让程序中没有因果关系的部分可以并发的执行
2. 改善用户体验 - 让耗时间的操作不会造成程序的假死
"""
import glob
import os
import threading

from PIL import Image

PREFIX = 'thumbnails'


def generate_thumbnail(infile, size, format='PNG'):
    """生成指定图片文件的缩略图"""
    file, ext = os.path.splitext(infile)
    file = file[file.rfind('/') + 1:]
    outfile = f'{PREFIX}/{file}_{size[0]}_{size[1]}.{ext}'
    img = Image.open(infile)
    img.thumbnail(size, Image.ANTIALIAS)
    img.save(outfile, format)


def main1():
    """主函数"""
    if not os.path.exists(PREFIX):
        os.mkdir(PREFIX)
        # print(glob.glob(r"/home/qiaoyunhao/*/*.png"), "\n")
        #  加上r让字符串不转义
        # 返回所有匹配的文件路径列表
    for infile in glob.glob('images/*.png'):
        for size in (32, 64, 128):
            # 创建并启动线程
            threading.Thread(
                target=generate_thumbnail,
                args=(infile, (size, size))
            ).start()


# if __name__ == '__main__':
#     main()


'''
线程  abc为函数
thread1 = threading.Thread(target=abc,args=(argv))
thread1.start()
thread1.join()
'''


#
# class acoun:
#     def __init__(self):
#         self.bnalce = 0.0
#         self.lock = threading.Lock
#     def despot(self,adds):
#         with self.lock:
#             self.bnalce += adds
#             self.lock

# #自定义线程类
# class addthread(threading.Thread):
#     def __init__(self,account,add):
#         self.account = account
#         self.add = add
#     def run(self):
#         self.account.deposit(1)

def test(value1, value2=None):
    print("%s threading is printed %s, %s\n"%(threading.current_thread().name, value1, value2))
    time.sleep(2)
    return 'finished'

def test_result(future):
    print(future.result())


import numpy as np
from concurrent.futures import ThreadPoolExecutor
threadPool = ThreadPoolExecutor(max_workers=4, thread_name_prefix="test_")
for i in range(0, 10):
    future = threadPool.submit(test, i, i+1)
threadPool.shutdown(wait=True)







# 多个线程竞争资源的情况。

"""
多线程程序如果没有竞争资源处理起来通常也比较简单
当多个线程竞争临界资源的时候如果缺乏必要的保护措施就会导致数据错乱
说明：临界资源就是被多个线程竞争的资源
"""
import time
import threading

from concurrent.futures import ThreadPoolExecutor


class Account(object):
    """银行账户"""

    def __init__(self):
        self.balance = 0.0
        self.lock = threading.Lock()

    def deposit(self, money):
        # 通过锁保护临界资源
        with self.lock:
            new_balance = self.balance + money
            time.sleep(0.001)
            self.balance = new_balance


class AddMoneyThread(threading.Thread):
    """自定义线程类"""

    def __init__(self, account, money):
        self.account = account
        self.money = money
        # 自定义线程的初始化方法中必须调用父类的初始化方法
        super().__init__()

    def run(self):
        # 线程启动之后要执行的操作
        self.account.deposit(self.money)

def main2():
    """主函数"""
    account = Account()
    # 创建线程池
    pool = ThreadPoolExecutor(max_workers=10)
    futures = []
    for _ in range(100):
        # 创建线程的第1种方式
        # threading.Thread(
        #     target=account.deposit, args=(1, )
        # ).start()
        # 创建线程的第2种方式
        # AddMoneyThread(account, 1).start()
        # 创建线程的第3种方式
        # 调用线程池中的线程来执行特定的任务
        future = pool.submit(account.deposit, 1)
        futures.append(future)
    # 关闭线程池
    pool.shutdown()


    for future in futures:
        future.result()
    print(account.balance)


# if __name__ == '__main__':
#     main2()

"""
多个线程竞争一个资源 - 保护临界资源 - 锁（Lock/RLock）
多个线程竞争多个资源（线程数>资源数） - 信号量（Semaphore）
多个线程的调度 - 暂停线程执行/唤醒等待中的线程 - Condition
"""
from concurrent.futures import ThreadPoolExecutor
from random import randint
from time import sleep

import threading


class Account():
    """银行账户"""

    def __init__(self, balance=0):
        self.balance = balance
        lock = threading.Lock()
        self.condition = threading.Condition(lock)
        # self.lock.acquire()加锁
        # self.lock.release()解锁

    def withdraw(self, money):
        """取钱"""
        with self.condition:
            while money > self.balance:
                self.condition.wait()
            new_balance = self.balance - money
            sleep(0.001)
            self.balance = new_balance

    def deposit(self, money):
        """存钱"""
        with self.condition:
            new_balance = self.balance + money
            sleep(0.001)
            self.balance = new_balance
            self.condition.notify_all()


def add_money(account):
    while True:
        money = randint(5, 10)
        account.deposit(money)
        print(threading.current_thread().name,
              ':', money, '====>', account.balance)
        sleep(0.5)


def sub_money(account):
    while True:
        money = randint(10, 30)
        account.withdraw(money)
        print(threading.current_thread().name,
              ':', money, '<====', account.balance)
        sleep(1)


def main3():
    account = Account()
    with ThreadPoolExecutor(max_workers=10) as pool:
        for _ in range(5):
            pool.submit(add_money, account)
            pool.submit(sub_money, account)


# if __name__ == '__main__':
#     main()

# 多进程：多进程可以有效的解决GIL的问题，实现多进程主要的类是Process，
# 其他辅助的类跟threading模块中的类似，进程间共享数据可以使用管道、
# 套接字等，在multiprocessing模块中有一个Queue类，它基于管道和锁机制
# 提供了多个进程共享的队列。下面是官方文档上关于多进程和进程池的一个示例。

"""
多进程和进程池的使用
多线程因为GIL的存在不能够发挥CPU的多核特性
对于计算密集型任务应该考虑使用多进程
time python3 example22.py
real    0m11.512s
user    0m39.319s
sys     0m0.169s
使用多进程后实际执行时间为11.512秒，而用户时间39.319秒约为实际执行时间的4倍
这就证明我们的程序通过多进程使用了CPU的多核特性，而且这台计算机配置了4核的CPU
"""
import concurrent.futures
import math

PRIMES = [
    1116281,
    1297337,
    104395303,
    472882027,
    533000389,
    817504243,
    982451653,
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419
] * 5


def is_prime(n):
    """判断素数"""
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def main4():
    """主函数"""
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))


# if __name__ == '__main__':
#     main4()
# 重点：多线程和多进程的比较。
#
# 以下情况需要使用多线程：
#
# 程序需要维护许多共享的状态（尤其是可变状态），Python中的列表、字典、集合都
# 是线程安全的，所以使用线程而不是进程维护共享状态的代价相对较小。
# 程序会花费大量时间在I/O操作上，没有太多并行计算的需求且不需占用太多的内存。
# 以下情况需要使用多进程：
#
# 程序执行计算密集型任务（如：字节码操作、数据处理、科学计算）。
# 程序的输入可以并行的分成块，并且可以将运算结果合并。
# 程序在内存使用方面没有任何限制且不强依赖于I/O操作（如：读写文件、套接字等）。

# 异步处理：从调度程序的任务队列中挑选任务，该调度程序以交叉的形式执行这些任务，
# 我们并不能保证任务将以某种顺序去执行，因为执行顺序取决于队列中的一项任务是否
# 愿意将CPU处理时间让位给另一项任务。异步任务通常通过多任务协作处理的方式来实现，
# 由于执行时间和顺序的不确定，因此需要通过回调式编程或者future对象来获取任务执行
# 的结果。Python 3通过asyncio模块和await和async关键字（在Python 3.7中正式被列为
# 关键字）来支持异步处理。

"""
异步I/O - async / await
"""
import asyncio


def num_generator(m, n):
    """指定范围的数字生成器"""
    yield from range(m, n + 1)


async def prime_filter(m, n):
    """素数过滤器"""
    primes = []
    for i in num_generator(m, n):
        flag = True
        for j in range(2, int(i ** 0.5 + 1)):
            if i % j == 0:
                flag = False
                break
        if flag:
            print('Prime =>', i)
            primes.append(i)

        await asyncio.sleep(0.001)
    return tuple(primes)


async def square_mapper(m, n):
    """平方映射器"""
    squares = []
    for i in num_generator(m, n):
        print('Square =>', i * i)
        squares.append(i * i)

        await asyncio.sleep(0.001)
    return squares


def main5():
    """主函数"""
    loop = asyncio.get_event_loop()
    future = asyncio.gather(prime_filter(2, 100), square_mapper(1, 100))
    future.add_done_callback(lambda x: print(x.result()))
    loop.run_until_complete(future)
    loop.close()

#
# if __name__ == '__main__':
#     main()
# 说明：上面的代码使用get_event_loop函数获得系统默认的事件循环，
# 通过gather函数可以获得一个future对象，future对象的add_done_callback
# 可以添加执行完成时的回调函数，loop对象的run_until_complete方法可以
# 等待通过future对象获得协程执行结果。
#
# Python中有一个名为aiohttp的三方库，它提供了异步的HTTP客户端和服务器，
# 这个三方库可以跟asyncio模块一起工作，并提供了对Future对象的支持。
# Python 3.6中引入了async和await来定义异步执行的函数以及创建异步上下文，
# 在Python 3.7中它们正式成为了关键字。下面的代码异步的从5个URL中获取页面
# 并通过正则表达式的命名捕获组提取了网站的标题。

import asyncio
import re

import aiohttp

PATTERN = re.compile(r'\<title\>(?P<title>.*)\/\<title\>')


async def fetch_page(session, url):
    async with session.get(url, ssl=False) as resp:
        return await resp.text()


async def show_title(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch_page(session, url)
        print(PATTERN.search(html).group('title'))


def main6():
    urls = ('https://www.python.org/',
            'https://git-scm.com/',
            'https://www.jd.com/',
            'https://www.taobao.com/',
            'https://www.douban.com/')
    loop = asyncio.get_event_loop()
    cos = [show_title(url) for url in urls]
    loop.run_until_complete(asyncio.wait(cos))
    loop.close()


# if __name__ == '__main__':
#     main()
# 重点：异步I/O与多进程的比较。
#
# 当程序不需要真正的并发性或并行性，而是更多的依赖于异步处理和回调时，
# asyncio就是一种很好的选择。如果程序中有大量的等待与休眠时，也应该考
# 虑asyncio，它很适合编写没有实时数据处理需求的Web应用服务器。
#
# Python还有很多用于处理并行任务的三方库，例如：joblib、PyMP等。实际开发
# 中，要提升系统的可扩展性和并发性通常有垂直扩展（增加单个节点的处理能力）
# 和水平扩展（将单个节点变成多个节点）两种做法。可以通过消息队列来实现应
# 用程序的解耦合，消息队列相当于是多线程同步队列的扩展版本，不同机器上的
# 应用程序相当于就是线程，而共享的分布式消息队列就是原来程序中的Queue。
# 消息队列（面向消息的中间件）的最流行和最标准化的实现是AMQP（高级消息队
# 列协议），AMQP源于金融行业，提供了排队、路由、可靠传输、安全等功能，最
# 著名的实现包括：Apache的ActiveMQ、RabbitMQ等。
#
# 要实现任务的异步化，可以使用名为Celery的三方库。Celery是Python编写的分
# 布式任务队列，它使用分布式消息进行工作，可以基于RabbitMQ或Redis来作为后
# 端的消息代理。
