#!/usr/bin/python3
# @Author: WLP
# @name: 进程.py
# @date 2020-04-08 16:10

from multiprocessing import Process
from random import randint
from os import getpid
from time import sleep, time

def download(name):
    print("开始下载%s" % name)
    sownload_time = randint(5,10)
    sleep(sownload_time)
    print("下载%s一共用了%d" % (name, sownload_time))
def main():
    start = time()
    p1 = Process(target=download, args=("file-1",))
    p2 = Process(target=download, args=("file-2",))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print(end-start)

if __name__ == '__main__':
    main()

