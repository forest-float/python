# -*- coding: utf-8 -*-
# @Author: wlp
# @Date:   2020-04-08 14:12:15
# @Last Modified by:   forest-float
# @Last Modified time: 2020-04-08 15:01:04

import _thread
import time

def thread_function(threadName, delay):
	n = 5
	while n > 0:
		time.sleep(delay)
		n -= 1
		print(time.ctime(time.time()), threadName)



try:
	_thread.start_new_thread(thread_function, ('thread1', 2))
	_thread.start_new_thread(thread_function, ('thread2', 4))
except:
	print("error ,can't create thread")


import threading


exitFlag = 0

class myThread(threading.Thread):
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter

	def run(self):
		print("开始线程：" + self.name)
		print(self.name, self.counter)
		time.sleep(5)
		print("退出线程：" + self.name)


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

#创建新线程
thread1 = myThread(1, "thread-1", 1)
thread2 = myThread(2, "thread-2", 2)

#开启进程
thread1.start()
thread2.start()
thread1.join()
thread2.join()


from time import sleep
from threading import Thread, Lock
#用于线程间的同步，相当于互斥锁，防止多个线程同时访问一块地址，造成数据错误

class Account(object):

    def __init__(self):
        self._balance = 0
        self._lock = Lock()#将这个变量设置为锁属性，等待获取锁acquire()和release()函数去加锁和解锁

    def deposit(self, money):
        # 先获取锁才能执行后续的代码
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance
        finally:
            # 在finally中执行释放锁的操作保证正常异常锁都能释放
            self._lock.release()

    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def main():
    account = Account()
    threads = []
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('账户余额为: ￥%d元' % account.balance)


if __name__ == '__main__':
    main()
