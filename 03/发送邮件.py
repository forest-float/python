#!/usr/bin/python3
# @Author: WLP
# @name: 发送邮件.py
# @date 2020-04-26 15:07

from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText

def main():
    sender = '1250683837@qq.com'
    receivers = ['1769873083@qq.com', '984236448@qq.com', '1250683837@qq.com', '1165541494@qq.com']
    #邮件内容
    message = MIMEText('用python发送邮件的实例代码', 'plain', 'utf-8')
    #发送者
    message['From'] = Header('吴林平', 'utf-8')
    #发送给谁
    message['To'] = Header('李成龙、夏彬、肖强', 'utf-8')
    #邮件的标题
    message['Subject'] = Header('示例代码实验邮件', 'utf-8')
    smtper = SMTP('smtp.qq.com')
    smtper.login(sender, 'bzrkurseymzvifeg')
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成')

if __name__ == '__main__':
    main()



