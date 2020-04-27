#!/usr/bin/python3
# @Author: WLP
# @name: 找出序列中出现最多的元素.py
# @date 2020-04-27 13:30

"""
找出序列中出现次数最多的元素
"""
from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
    'look', 'into', 'my', 'eyes', "you're", 'under'
]
counter = Counter(words)
print(counter.most_common(3))
#获取出现频率最高的三个元素

ms = set(words)
m = map(words.count, ms)
ml = list(m)
print(ml)
z = zip(ms, ml)
zl = list(z)
print(zl)


