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
# if __name__ == "__main__":
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



class downloader(object):

    def __init__(self):
        self.server = 'http://www.biqukan.com/'
        self.target = 'http://www.biqukan.com/1_1094/'
        self.names = []            #存放章节名
        self.urls = []            #存放章节链接
        self.nums = 0            #章节数

    """
    函数说明:获取下载链接
    Parameters:
        无
    Returns:
        无
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
        self.nums = len(a[15:])                                #剔除不必要的章节，并统计章节数
        for each in a[15:]:
            self.names.append(each.string)
            self.urls.append(self.server + each.get('href'))

    """
    函数说明:获取章节内容
    Parameters:
        target - 下载连接(string)
    Returns:
        texts - 章节内容(string)
    Modify:
        2017-09-13
    """
    def get_contents(self, target):
        req = requests.get(url = target)
        html = req.text
        bf = BeautifulSoup(html, features="lxml")
        texts = bf.find_all('div', class_ = 'showtxt')
        texts = texts[0].text.replace('\xa0'*8, '\n\n')
        return texts

    """
    函数说明:将爬取的文章内容写入文件
    Parameters:
        name - 章节名称(string)
        path - 当前路径下,小说保存名称(string)
        text - 章节内容(string)
    Returns:
        无
    Modify:
        2017-09-13
    """
    def writer(self, name, path, text):
        write_flag = True
        with open(path, 'a', encoding='GBK') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')

if __name__ == "__main__":
    dl = downloader()
    dl.get_download_url()
    print('《一年永恒》开始下载：')
    for i in range(dl.nums):
        dl.writer(dl.names[i], '一念永恒.txt', dl.get_contents(dl.urls[i]))
        sys.stdout.write("  已下载:%.3f%%" %  float(i/dl.nums) + '\r')
        sys.stdout.flush()
    print('《一年永恒》下载完成')
