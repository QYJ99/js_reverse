# -*- coding: utf-8 -*-
# @Time    : 2022/1/11 15:21
# @Author  : Cat
# @FileName: weibo_login.py

import requests
import execjs

headers = {
    'Host': 'login.sina.com.cn',
    'Referer': 'https://www.weibo.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
}
s = requests.Session()
s.get('https://www.weibo.com/login.php',headers=headers)


prelogin_url = 'https://login.sina.com.cn/sso/prelogin.php?entry=account&su=MTM1Mzk1NjA5OTE%3D&rsakt=mod&client=ssologin.js(v1.4.15)&_=1641889555300'
res = s.get(prelogin_url,headers=headers)
print(res.text)
res_josn = res.json()
#

rsaPubkey = res_josn['pubkey']
servertime = res_josn['servertime']
nonce = res_josn['nonce']
rsakv = res_josn['rsakv']
b = 'qqqq12345678'

with open("./encrpypt.js","r", encoding="utf-8") as f:  # spiders/module/
    js_code = f.read()
ctx = execjs.compile(js_code,)

sp = ctx.call("get_sp",rsaPubkey,servertime,nonce,b)
print(sp)


login_url = 'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.15)&_=1641889555325'

login_data = {
    'entry': 'account',
    'gateway': '1',
    'from': '',
    'savestate': '0',
    'useticket': '0',
    'pagerefer': '',
    'vsnf': '1',
    'su': 'MsdwASDSDE=',
    'service': 'account',
    'servertime': servertime,
    'nonce': nonce,
    'pwencode': 'rsa2',
    'rsakv': rsakv,
    'sp': sp,
    'sr': '1920*1080',
    'encoding': 'UTF-8',
    'cdult': '3',
    'domain': 'sina.com.cn',
    'prelt': '11',
    'returntype': 'TEXT',
}

login_res = s.post(login_url,headers=headers,data=login_data)
# login_res.encoding = "GBK"
print(login_res.text.encode('utf-8').decode('unicode_escape'))







