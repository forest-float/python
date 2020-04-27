#初始化16*16的点阵位置，每个汉字需要16*16=256个点来表示
rect_list = [] * 16
for i in range(16):
    rect_list.append([] * 16)
#拿赞字来演示
text = "赞"
#获取中文编码
import binascii
gb2312zan = text.encode('gb2312')
hex_str = binascii.b2a_hex(gb2312zan)
result = str(hex_str, encoding='utf-8')

#根据编码计算“赞”字在汉字库中的位置
area = eval('0x' + result[:2]) - 0xA0
index = eval('0x' + result[2:]) - 0xA0
offset = (94 * (area-1) + (index-1)) * 32
font_rect = None
#读取HZK16汉字库文件中“赞”字数据
with open("HZK16", 'rb') as f:     #相当于  f = open("HZK16",'rb'),且自动包含close，防止打开文件失败
    f.seek(offset)
    font_rect = f.read(32)
#根据读取到HZK中数据给我们的16*16点阵赋值
for k in range(len(font_rect) // 2):
    row_list = rect_list[k]
    for j in range(2):
        for i in range(8):
            asc = font_rect[k * 2 + j]
            flag = asc & 1
            row_list.append(flag)
#根据获取到的16*16点阵信息，打印到控制台
for row in rect_list:
    for i in row:
        if i:
            #前景字符（即用来表示汉字笔画的输出字符）
            print('0', end=' ')
        else:
            #背景字符（即用来表示背景的输出字符）
            print('.', end=' ')
print()
from PIL import Image

#通过二维码登录微信网页版
#pip install itchat
import itchat
itchat.auto_login()
#获取微信好友信息列表
friendList = itchat.get_friends(update=True)
#读取好友头像
for friend in friendList:
    friend['head_img'] = itchat.get_head_img(userName=friend['UserName'])
    friend['head_img_name'] = "%s.jpg" % friend['UserName']
    #写入文件
    with open(friend['head_img_name'],'wb') as f:
        f.write(friend['head_img'])
#新建画布，16*16点阵，每个图片边长100

'''1.更新pip
pip --version 查看pip版本
python -m pip install --upgrade pip 更新pip

2.安装python的PIL(图像处理库)
pip install Pillow

3.python应用导入PIL
import PIL.Image
'''

#pip install pillow -i https://pypi.tuna.tsinghua.edu.cn/simple/
canvas = Image.new('RGB', (1600, 1600), '#FFFFFF')
n = 0
for i in range(16*16):
    #点阵信息为1，即代表此处要显示头像来组字
    if item[i] == "1":
        # 打开图片
        img = Image.open(imgList[n])
        # 缩小图片
        img = img.resize((100, 100), Image.ANTIALIAS)
        # 拼接图片
        canvas.paste(img, ((i % 16) * 100, (i // 16) * 100))
        n += 1


