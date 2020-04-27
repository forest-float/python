#!/usr/bin/python3
# @Author: WLP
# @name: 排列组合.py
# @date 2020-04-27 11:54
#迭代工具模块
import itertools

# 产生ABCD的全排列
print(list(itertools.permutations('ABCD')).__len__())
# 产生ABCDE的五选三组合
print(list(itertools.combinations('ABCDE', 3)))
# 产生ABCD和123的笛卡尔积
print(list(itertools.product('ABCD', '123')))
# 产生ABC的无限循环序列
#print(list(itertools.cycle(('A', 'B', 'C'))))



