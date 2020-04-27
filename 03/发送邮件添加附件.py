#!/usr/bin/python3
# @Author: WLP
# @name: 发送邮件添加附件.py
# @date 2020-04-26 15:48

from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

import urllib


def main():
    # 创建一个带附件的邮件消息对象
    message = MIMEMultipart()

    # 创建文本内容
    text_content = MIMEText('附件中有本月数据请查收', 'plain', 'utf-8')
    # 发送者
    message['From'] = Header('吴林平', 'utf-8')
    # 发送给谁
    message['To'] = Header('李成龙、夏彬、肖强', 'utf-8')
    message['Subject'] = Header('本月数据', 'utf-8')
    # 将文本内容添加到邮件消息对象中
    message.attach(text_content)

    # 读取文件并将文件作为附件添加到邮件消息对象中
    with open('hello.txt', 'rb') as f:
        txt = MIMEText(f.read(), 'base64', 'utf-8')
        txt['Content-Type'] = 'text/plain'
        txt['Content-Disposition'] = 'attachment; filename=hello.txt'
        message.attach(txt)
    # 读取文件并将文件作为附件添加到邮件消息对象中
    with open('汇总数据.xlsx', 'rb') as f:
        xls = MIMEText(f.read(), 'base64', 'utf-8')
        xls['Content-Type'] = 'application/vnd.ms-excel'
        xls['Content-Disposition'] = 'attachment; filename=month-data.xlsx'
        message.attach(xls)


    # 开启安全连接
    # smtper.starttls()
    sender = '1250683837@qq.com'
    receivers = ['1769873083@qq.com', '984236448@qq.com', '1250683837@qq.com', '1165541494@qq.com']
    smtper = SMTP('smtp.qq.com')
    smtper.login(sender, 'bzrkurseymzvifeg')
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成')
    # 与邮件服务器断开连接
    smtper.quit()



if __name__ == '__main__':
    main()



