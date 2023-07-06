# -*- coding: utf-8 -*-
# @Time    : 2022/1/11 11:16
# @Author  : Cat
# @FileName: 10086_login.py

import time
import execjs
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Host': 'login.10086.cn',
    'Origin': 'https://login.10086.cn',
    'Referer': 'https://login.10086.cn/html/login/email_login.html?channelID=12014&backUrl=http://touch.10086.cn/i',
}

s = requests.Session()
s.get('https://login.10086.cn/html/login/email_login.html?',headers=headers)

t = int(time.time() * 1000)
code_url = 'https://login.10086.cn/captchazh.htm?type=03&timestamp={}'.format(t)
code_res = s.get(code_url,headers=headers)

img = code_res.content
with open('./1.img', 'wb') as f:
    f.write(img)
code = input('输入验证码：')


with open("./encrpypt.js","r", encoding="utf-8") as f:  # spiders/module/
    js_code = f.read()
ctx = execjs.compile(js_code,)

username_str = "123456789@qq.com"
password_str = 'qq123456789'
username = ctx.call("encrypt_10086",username_str)
password = ctx.call("encrypt_10086",password_str)

# 加密的结果
print(username)
print(password)

url = 'https://login.10086.cn/login.htm'

data = {
    'accountType': '02',
    'pwdType': '03',
    'account': username,
    'password': password,
    'inputCode': code,
    'backUrl': 'http://touch.10086.cn/i',
    'rememberMe': '0',
    'channelID': '12014',
    'protocol': 'https:',
    'loginMode': '03',
    'timestamp': '1641816775943',
}

res = s.post(url,data=data,headers=headers)

print(res.text)