#!/usr/bin/python3
# @Author: WLP
# @name: 使用多进程对复杂任务进行分化.py
# @date 2020-04-08 17:16

from multiprocessing import Process, Queue
from random import randint
from time import time


def task_handler(curr_list, result_queue):
    total = 0
    for number in curr_list:
        total += number
    result_queue.put(total)#用于给队列中添加数据


def main():
    processes = []
    number_list = [x for x in range(1, 1000001)]
    result_queue = Queue()#队列，FIFO
    index = 0
    # 启动8个进程将数据切片后进行运算
    start = time()
    for _ in range(8):
        p = Process(target=task_handler,
                    args=(number_list[index:index + 125000], result_queue))
        index += 12500000
        processes.append(p)
        p.start()
    # 开始记录所有进程执行完成花费的时间

    for p in processes:

        p.join()
    # 合并执行结果
    total = 0
    while not result_queue.empty():
        total += result_queue.get()
    print(total)
    end = time()
    print('Execution time: ', (end - start), 's', sep='')


if __name__ == '__main__':
    main()

