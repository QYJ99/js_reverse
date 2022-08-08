# -*- coding: utf-8 -*-
# @Time    : 2022/8/8 16:41
# @Author  : Cat
# @FileName: login.py
import re
import requests
import execjs

cookies = {
    'Hm_lvt_1287c2225a527abe3386233dd9316f99': '1659941378',
    'Hm_lpvt_1287c2225a527abe3386233dd9316f99': '1659941378',
    'SSO-KGZLT': '49084b8a-52f2-4ea1-be74-40821ec99a9e',
    'SSO-KGZQRT': 'F86106CA415A8488578ECAA95B57327D',
    'KZLBS': 'd7d10e488a0e2047',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,zh-HK;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'Hm_lvt_1287c2225a527abe3386233dd9316f99=1659941378; Hm_lpvt_1287c2225a527abe3386233dd9316f99=1659941378; SSO-KGZLT=49084b8a-52f2-4ea1-be74-40821ec99a9e; SSO-KGZQRT=F86106CA415A8488578ECAA95B57327D; KZLBS=d7d10e488a0e2047',
    'Pragma': 'no-cache',
    'Referer': 'https://passport.kongzhong.com/',
    'Sec-Fetch-Dest': 'script',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://sso.kongzhong.com/ajaxLogin?j=j&jsonp=j&service=https://passport.kongzhong.com/&_=1659941661420', headers=headers) # cookies=cookies,
dc = re.findall('"dc":"(.*?)"',str(response.text))[0]
print(dc)


with open("./login_encrypt.js","r", encoding="utf-8") as f:  # spiders/module/
    js_code = f.read()
ctx = execjs.compile(js_code,) #cwd="C:/Users/thouger/AppData/Roaming/npm/node_modules"

pwd = ctx.call("get_pwd",'123456789',dc)
print(pwd)



login = requests.get('https://sso.kongzhong.com/ajaxLogin?j=j&&type=1&service=https://passport.kongzhong.com/&username=12343432423&password={}&vcode=r0p6&toSave=0&_=1659941671159'.format(pwd), cookies=cookies, headers=headers)

print(login.text)
