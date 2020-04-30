#!/usr/bin/python3
# @Author: WLP
# @name: condition使用.py
# @date 2020-04-28 14:19

import threading

'''Condition机制:条件同步，用户复杂的线程间同步。内部使用的也是lock或者Rlock'''
'''
wait(timeout=None)
当前线程等待着另外的线程发起通知，才向下执行。
notify()   
发出通知
notify_all通知所有的condition
'''
"""
张三：床前明月光
李四：疑是地上霜
张三：举头望明月
李四：低头思故乡

怎么实现两个线程的交替说话，如果只有两句，可以使用锁机制，让某个线程先执行，这里有多句话交替出现，最好使用condition
"""


class ZSThead(threading.Thread):
    def __init__(self, name, cond):
        super(ZSThead, self).__init__()
        self.name = name
        self.cond = cond

    def run(self):
        # 必须先调用with self.cond，才能使用wait()、notify()方法
        with self.cond:
            # 讲话
            print("{}:床前明月光".format(self.name))
            # 等待李四的回应
            self.cond.notify()
            self.cond.wait()

            # 讲话
            print("{}:举头望明月".format(self.name))
            # 等待李四的回应
            self.cond.notify()
            self.cond.wait()


class LSThread(threading.Thread):
    def __init__(self, name, cond):
        super(LSThread, self).__init__()
        self.name = name
        self.cond = cond

    def run(self):
        with self.cond:
            # wait()方法不仅能获得一把锁，并且能够释放cond的大锁，这样张三才能进入with self.cond中
            self.cond.wait()
            print(f"{self.name}:疑是地上霜")
            # notify()释放wait()生成的锁
            self.cond.notify()

            self.cond.wait()
            print(f"{self.name}:低头思故乡")
            self.cond.notify()


cond = threading.Condition()
zs = ZSThead("张三", cond)
ls = LSThread("李四", cond)

# 启动顺序很重要，必须先启动李四，让他在那里等待着，
# 因为先启动张三时，他说了话就发出了通知，但是当时李四的进程还没有启动，
# 并且condition外面的大锁也没有释放，李四也没法获取self.cond这把大锁
# condition有两层锁，一把底层锁在线程调用了wait()方法就会释放
# 每次调用wait()方法后，都会创建一把锁放进condition的双向队列中，等待notify()方法的唤醒
ls.start()
zs.start()



