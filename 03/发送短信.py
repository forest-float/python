#!/usr/bin/python3
# @Author: WLP
# @name: 发送短信.py
# @date 2020-04-26 15:45

'''
发送短信也是项目中常见的功能，网站的注册码、验证码、
营销信息基本上都是通过短信来发送给用户的。在下面的
代码中我们使用了互亿无线短信平台（该平台为注册用户
提供了50条免费短信以及常用开发语言发送短信的demo，
可以登录该网站并在用户自服务页面中对短信进行配置）
提供的API接口实现了发送短信的服务，当然国内的短信
平台很多，读者可以根据自己的需要进行选择（通常会
考虑费用预算、短信达到率、使用的难易程度等指标），
如果需要在商业项目中使用短信服务建议购买短信平台
提供的套餐服务。
'''
import urllib.parse
import http.client
import json


def main():
    host  = "106.ihuyi.com"
    sms_send_uri = "/webservice/sms.php?method=Submit"
    # 下面的参数需要填入自己注册的账号和对应的密码
    params = urllib.parse.urlencode({'account': '你自己的账号', 'password' : '你自己的密码', 'content': '您的验证码是：147258。请不要把验证码泄露给其他人。', 'mobile': '接收者的手机号', 'format':'json' })
    print(params)
    headers = {'Content-type': 'application/x-www-form-urlencoded', 'Accept': 'text/plain'}
    conn = http.client.HTTPConnection(host, port=80, timeout=30)
    conn.request('POST', sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    jsonstr = response_str.decode('utf-8')
    print(json.loads(jsonstr))
    conn.close()


if __name__ == '__main__':
    main()



