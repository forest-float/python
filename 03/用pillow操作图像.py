#!/usr/bin/python3
# @Author: WLP
# @name: 用pillow操作图像.py
# @date 2020-04-26 16:06

'''
Pillow是由从著名的Python图像处理库PIL发展出来的一个分支，
通过Pillow可以实现图像压缩和图像处理等各种操作。可以使用
下面的命令来安装Pillow。
pip install pillow
'''
from PIL import Image

image = Image.open('1.png')
#后缀，  大小，  颜色类型
print(image.format, image.size, image.mode)
image.show()#用默认程序打开图片

# 裁剪
# rect = 80, 20, 310, 360
# image.crop(rect).show()

# 生成缩略图
# size = 128, 128
# image.thumbnail(size)
# image.show()

# 缩放和黏贴图像
# rect = 80, 20, 310, 360
# guido_head = image.crop(rect)
# width, height = guido_head.size
# image.paste(guido_head.resize((int(width / 1.5), int(height / 1.5))), (172, 40))

# 旋转和翻转
# image.rotate(180).show()
# image.transpose(Image.FLIP_LEFT_RIGHT).show()

#操作像素
# for x in range(80, 310):
#     for y in range(20, 360):
#         image.putpixel((x, y), (128, 128, 128))

#滤镜效果
# from PIL import Image, ImageFilter
# #
# image.filter(ImageFilter.CONTOUR).show()

