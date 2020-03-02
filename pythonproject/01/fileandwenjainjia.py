# -*- coding: utf-8 -*-
import os,shutil
import sys
import numpy as np
#安装numpy库需要先要用cd命令进入Python安装界面，然后pip install numpy


##########批量删除不同文件夹下的同名文件夹#############
def arrange_file(dir_path0):
    for dirpath,dirnames,filenames in os.walk(dir_path0):
        if 'my_result' in dirpath:
           # print(dirpath)
            shutil.rmtree(dirpath)


##########批量在不同文件夹下新建同名子文件夹并把文件搬移到子文件夹#############
def arrange_file(dir_path0):
    for dirpath,dirnames,filenames in os.walk(dir_path0):
        for files in filenames:
            total_path = os.path.join(dirpath,files)
            root_path,file_path = total_path.split(dir_path,1)
            if 'png' in file_path:
                new_file_path = '.' + file_path[:-9] + 'new_file_name/'
                # print(file_path)
                # print(new_file_path)
                # print(new_file_path + file_path[-9:])
                # if not os.path.exists(new_file_path):
                #     os.makedirs(new_file_path)
                # shutil.move('.' + file_path,new_file_path + file_path[-9:])

##########批量删除不同文件夹下符合条件的文件##################
def arrange_file(dir_path0):
    for dirpath,dirnames,filenames in os.walk(dir_path0):
        for files in filenames:
            total_path = os.path.join(dirpath,files)
            # print(total_path)
            if 'jpg' in total_path and 'labels' in total_path:
                img = cv2.imread(total_path)
                if np.sum(img) == 0:
                    print(total_path)
                    os.remove(total_path)

###########批量把文件搬移到上一层文件夹并删除当前文件夹########
def arrange_file(dir_path0):
    for dirpath,dirnames,filenames in os.walk(dir_path0):
        for files in filenames:
            total_path = os.path.join(dirpath,files)
            root_path,file_path = total_path.split(dir_path0,1)
            # print(file_path[:-48])
            # return 0
            if 'jpg' in file_path:
                new_file_path = dir_path0 + file_path[:-48]
                shutil.move(dir_path0 + file_path,new_file_path + file_path[-9:])

    for dirpath,dirnames,filenames in os.walk(dir_path0):
        file_path = dirpath.split('./your_total_path')[1]
        if 'keywords' in file_path:
           # print(dirpath)
            shutil.rmtree(dirpath)


