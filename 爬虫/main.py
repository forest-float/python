#!/usr/bin/python3
# @Author: WLP
# @name: main.py
# @date 2020-03-31 15:23

import requests
from bs4 import BeautifulSoup
import os

target = 'https://www.biqukan.com/1_1094/5403177.html'
req = requests.get(url=target)
req.encoding = "GBK"
html = req.text
# print(req.text)
with open("text.txt", "r+", encoding="GBK") as fil:
    fil.write(req.text)
    # print(fil.read())
    
    
    bf = BeautifulSoup(fil.read(), features="lxml")
    texts = bf.find_all('div', class_='showtxt')
    # print(texts[0].text.replace('\xa0'*8, ' '))
    # print(texts)
if __name__ == "__main__":
    server = 'http://www.biqukan.com/'
    target = 'http://www.biqukan.com/1_1094/'
    req = requests.get(url = target)
    req.encoding = "GBK"
    html = req.text

    div_bf = BeautifulSoup(html, features="lxml")
    div = div_bf.find_all('div', class_ = 'listmain')

    #print(div[0])
    a_bf = BeautifulSoup(str(div[0]), features="lxml")
    a = a_bf.find_all('a')
for each in a:
    print(each.string, server + each.get('href'))
print(each)


"""
��˵��:���ء���Ȥ������С˵��һ�����㡷
Parameters:
    ��
Returns:
    ��
Modify:
    2017-09-13
"""
class downloader(object):

    def __init__(self):
        self.server = 'http://www.biqukan.com/'
        self.target = 'http://www.biqukan.com/1_1094/'
        self.names = []            #����½���
        self.urls = []            #����½�����
        self.nums = 0            #�½���

    """
    ����˵��:��ȡ��������
    Parameters:
        ��
    Returns:
        ��
    Modify:
        2017-09-13
    """
    def get_download_url(self):
        req = requests.get(url = self.target)
        html = req.text
        div_bf = BeautifulSoup(html)
        div = div_bf.find_all('div', class_ = 'listmain')
        a_bf = BeautifulSoup(str(div[0]), features="lxml")
        a = a_bf.find_all('a')
        self.nums = len(a[15:])                                #�޳�����Ҫ���½ڣ���ͳ���½���
        for each in a[15:]:
            self.names.append(each.string)
            self.urls.append(self.server + each.get('href'))

    """
    ����˵��:��ȡ�½�����
    Parameters:
        target - ��������(string)
    Returns:
        texts - �½�����(string)
    Modify:
        2017-09-13
    """
    def get_contents(self, target):
        req = requests.get(url = target)
        html = req.text
        bf = BeautifulSoup(html)
        texts = bf.find_all('div', class_ = 'showtxt')
        texts = texts[0].text.replace('\xa0'*8,'\n\n')
        return texts

    """
    ����˵��:����ȡ����������д���ļ�
    Parameters:
        name - �½�����(string)
        path - ��ǰ·����,С˵��������(string)
        text - �½�����(string)
    Returns:
        ��
    Modify:
        2017-09-13
    """
    def writer(self, name, path, text):
        write_flag = True
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')

if __name__ == "__main__":
    dl = downloader()
    dl.get_download_url()
    print('��һ�����㡷��ʼ���أ�')
    for i in range(dl.nums):
        dl.writer(dl.names[i], 'һ������.txt', dl.get_contents(dl.urls[i]))
        sys.stdout.write("  ������:%.3f%%" %  float(i/dl.nums) + '\r')
        sys.stdout.flush()
    print('��һ�����㡷�������')
