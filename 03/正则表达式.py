# -*- coding: utf-8 -*-
# @Author: wlp
# @Date:   2020-04-20 16:49:26
# @Last Modified by:   forest-float
# @Last Modified time: 2020-04-22 15:15:19

import re


def main():
    # 创建正则表达式对象 使用了前瞻和回顾来保证手机号前后不应该出现数字
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    sentence = " 重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，\
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。"
    
    
    # 查找所有匹配并保存到一个列表中
    # mylist = re.findall(pattern, sentence)
    listphone = []
    phonename = re.findall(r'[，。]\D{1,3}(?=的手机号)',sentence)
    for phone in phonename:
    	phonenames = re.sub(r'[,，]','',phone,flags=re.I)
    	listphone.append(phonenames)

    print(listphone)
    mylist = pattern.findall(sentence)
    print(mylist)
    print(list(zip(listphone,mylist)))
    print('--------华丽的分隔线--------')

    # 通过迭代器取出匹配对象并获得匹配的内容
    # 相当于for temp in re.finditer(pattern,sentence):
    for temp in pattern.finditer(sentence):
        print(temp.group())
    print('--------华丽的分隔线--------')

    # 通过search函数指定搜索位置找出所有匹配
    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence, m.end())


    sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
    purified = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔',
                      '*', sentence, flags=re.I)
    print(purified)  # 你丫是*吗? 我*你大爷的. * you.

    poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
    sentence_list = re.split(r'[，。, .]', poem)
    while '' in sentence_list:
        sentence_list.remove('')
    print(sentence_list)  # ['窗前明月光', '疑是地上霜', '举头望明月', '低头思故乡']

if __name__ == '__main__':
    main()

