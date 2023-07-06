# -*- coding: utf-8 -*-
# @Time    : 2022/7/29 11:42
# @Author  : Cat
# @FileName: yiban_login.py

import re
import time
import execjs
import requests

s = requests.Session()
index_res = s.get("https://www.yiban.cn/login?").text
captcha_path_url = re.findall('<img class="captcha" src="(.*?)" >',index_res)[0]


headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9,zh-HK;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'https_waf_cookie=f8c36695-0b62-48f99c9d50db9d3879485b6a52a132003364; YB_SSID=ad86cec374934bbaa4086b91f9f6e878',
    'Origin': 'https://www.yiban.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://www.yiban.cn/login?',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
captcha_url = f'https://www.yiban.cn/captcha/index?{captcha_path_url}'
print(captcha_url)
print(time.time())
with open("checkCode.png", "wb") as f:
    f.write(s.get(captcha_url,).content)

captcha = input('请输入验证码：') # 后期可以改为用验证码识别

with open("./encrypt.js","r", encoding="utf-8") as f:  # spiders/module/
    js_code = f.read()
ctx = execjs.compile(js_code,) #cwd="C:/Users/thouger/AppData/Roaming/npm/node_modules"

pwd = ctx.call("getpwd",'123456789')


data = {
    'account': 'ere124354213ewe',
    'password': pwd,
    'captcha': captcha,
    # 'keysTime': '1659062907.2',
    'is_rember': '1',
}

response = s.post('https://www.yiban.cn/login/doLoginAjax', data=data) #cookies=cookies, headers=headers,
print(response.json())
