# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 11:22:19 2018

@author: Yangzj
"""
import requests
import os
from bs4 import BeautifulSoup
import json
import time

'''
def login():
    url = 'http://www.zhihu.com'
    loginURL = 'http://www.zhihu.com/login/email'
    headers = {
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:41.0) Gecko/20100101 Firefox/41.0',
        "Referer": "http://www.zhihu.com/",
        'Host': 'www.zhihu.com',
    }
    data = {
        'email': '317493138@qq.com',
        'password': 'YANG19911118',
        'rememberme': "true",
    }
    global s
    s = requests.session()
    global xsrf
    if os.path.exists('cookiefile'):
        with open('cookiefile') as f:
            cookie = json.load(f)
        s.cookies.update(cookie)
        req1 = s.get(url, headers=headers)
        soup = BeautifulSoup(req1.text, "html.parser")
        xsrf = soup.find('input', {'name': '_xsrf', 'type': 'hidden'}).get('value')
        # 建立一个zhihu.html文件,用于验证是否登陆成功
        with open('zhihu.html', 'w') as f:
            f.write(req1.content)
    else:
        req = s.get(url, headers=headers)
        print(req)
        soup = BeautifulSoup(req.text, "html.parser")
        xsrf = soup.find('input', {'name': '_xsrf', 'type': 'hidden'}).get('value')
        data['_xsrf'] = xsrf
        timestamp = int(time.time() * 1000)
        captchaURL = 'http://www.zhihu.com/captcha.gif?=' + str(timestamp)
        print(captchaURL)
        with open('zhihucaptcha.gif', 'wb') as f:
            captchaREQ = s.get(captchaURL, headers=headers)
            f.write(captchaREQ.content)
        loginCaptcha = input('input captcha:\n').strip()
        data['captcha'] = loginCaptcha
        print(data)
        loginREQ = s.post(loginURL, headers=headers, data=data)
        if not loginREQ.json()['r']:
            print(s.cookies.get_dict())
            with open('cookiefile', 'wb') as f:
                json.dump(s.cookies.get_dict(), f)
        else:
            print('login fail')
            
login()            
'''


########先登录豆瓣，把cookie复制放在cookie.txt
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0','Connection':'keep-alive'}

absolute_url="https://www.zhihu.com/question/49883187/answer/291073428"
f_cookies = open('cookiezh.txt', 'r')
cookies = {}
for line in f_cookies.read().split(';'):
    name, value = line.strip().split('=', 1)
    cookies[name] = value
html = requests.get(absolute_url, cookies=cookies, headers=header)#.content


txt=html.content.decode("utf8")

print("xx")                   
print(txt)                   