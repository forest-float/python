#!/usr/bin/python3
# @Author: WLP
# @name: 约瑟夫问题.py
# @date 2020-05-07 16:41

def move(man, sep):
    for i in range(sep):
        item = man.pop(0)
        man.append(item)

def play(man=41, sep=3, rest=2):
    man = [i for i in range(1,man+1)]
    sep -= 1
    while len(man) > rest:
        move(man, sep)
        print("kill %d" % man.pop(0))
    print(man)

if __name__ == '__main__':
    play()



