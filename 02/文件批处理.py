#!/usr/bin/python3
# @Author: WLP
# @name: 文件批处理.py
# @date 2020-03-30 14:38

#批处理文件
import os
import shutil

file_names = os.listdir("./")
print(file_names)
try:
    os.mkdir("section1")
    os.mkdir("section2")
    os.mkdir("section3")
except FileExistsError:
    print('文件夹已经存在')
i = 0
for file_name in file_names:
    splited_file_name = file_name.split('.')
    print(splited_file_name)
    if  splited_file_name[0] == 'idea' \
            or 'section' in splited_file_name[0] \
            or splited_file_name[1] != 'bmp':
        continue
    #file_id = int(splited_file_name[0])
    #size_folder = "section"+str((file_id-1)%3+1)
    #shutil.move(file_name, os.path.join(os.getcwd(), file_name))

    os.renames(file_name, str(i)+'.png')#更改名字
    shutil.copyfile(str(i)+'.png', file_name)  # 复制文件

#move(src, dst)： 将src移动至dst目录下。若dst目录不存在，则效果等同于src改名为dst。
#若dst目录存在，将会把src文件夹的所有内容移动至该目录下面
#os.path.join()函数用于路径拼接文件路径。
#os.path.join()函数中可以传入多个路径：
#会从第一个以”/”开头的参数开始拼接，之前的参数全部丢弃。
#以上一种情况为先。在上一种情况确保情况下，若出现”./”开头的参数，
# 会从”./”开头的参数的上一个参数开始拼接。
#使用os.getcwd()函数获得当前的路径。


