#!/usr/bin/python3
# @Author: WLP
# @name: download.py
# @date 2020-04-01 9:24

from bs4 import BeautifulSoup
import requests
import sys

class download:
    def __init__(self, server, target):
        self.server = server
        self.target = target
        self.name = []
        self.url = []
        self.num = 0

    def get_download_url(self):
        download_url = requests.get(url = self.target)
        download_url.encoding = "GBK"
        req_text = download_url.text
        html = BeautifulSoup(req_text, features="lxml")
        div = html.find_all("div", class_="listmain")
        a_bf = BeautifulSoup(str(div[0]), features="lxml")
        a_data = a_bf.find_all('a')
        self.num = len(a_data[13:])
        for a_url in a_data[13:]:
            self.name.append(a_url.string)
            self.url.append(self.server + a_url.get("href"))

        #print(list(zip(self.name, self.url)))

    def get_content(self, send_url):
        req = requests.get(url = send_url)
        req.encoding = "GBK"
        html = req.text
        html_data = BeautifulSoup(html, features="lxml")
        textdata = html_data.find_all('div', class_ = "showtxt")
        text = textdata[0].text.replace('\xa0'*8, '\n')
        print(text)
        return text

    def write_data(self, name):
        print("开始下载" + name)
        with open(name, 'a+', encoding="UTF-8") as file:
            for num in range(self.num):
                sys.stdout.write("\r{0}{1}".format("已下载:",'%.3f%%' % float(num / self.num *100)))
                sys.stdout.flush()
                file.write(self.name[num] + '\n')
                data = self.get_content(self.url[num])
                file.writelines(data)
                file.write('\n\n')
        print(name + "下载完成")




server = 'http://www.biqukan.com/'
target = 'http://www.biqukan.com/1_1094/'
down = download(server, target)
down.get_download_url()
down.write_data("一念永恒.txt")