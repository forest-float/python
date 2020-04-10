import cv2
import os
 
 
 
file_path = ("拼手速.mp4")    #读取视频路径
#如果没有img文件夹就创建一个img文件夹
if not os.path.exists("img"):
    os.mkdir("img")
print("正在处理：",file_path)    #显示正在处理的视频文件
vidcap = cv2.VideoCapture(file_path)  #VideoCapture()打开视频路径
success,image = vidcap.read()    #第一个返回值为是否成功获取视频帧，第二个返回值为返回的视频帧
count = 0   #设置变量0来计数
success = True
while success:
    success,image = vidcap.read()
    try:
        cv2.imwrite(r"img/img_%d.jpg" % count, image)    #保存图片
        print("正在生成第",count,"张图片")
        if cv2.waitKey(10) == 27:    #waitKey()–是在一个给定的时间内(单位ms)等待用户按键触发; 如果用户没有按下键,则接续等待(循环)，用户按下ESC(ASCII码为27),执行if体
            break    #打破循环，也就是终止循环
    except Exception as e:
        print(e)
    count += 1    #count = count + 1  每次增加1