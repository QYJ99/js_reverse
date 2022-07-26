# -*- coding: utf-8 -*-
# @Time    : 2022/7/26 15:56
# @Author  : Cat
# @FileName: hnzwfw_login.py

import requests
import execjs

# 目标网址
# https://login.hnzwfw.gov.cn/tacs-uc/login/index

cookies = {
        'SESSION': 'Mjg3ZTU4ZDQtOTRmYi00MmE5LWExMGEtMDhhZGQ3MTcxNGRm',
    }
headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,zh-HK;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Origin': 'https://login.hnzwfw.gov.cn',
        'Pragma': 'no-cache',
        'Referer': 'https://login.hnzwfw.gov.cn/tacs-uc/login/index',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }


def start_login():
    # csrfsave_data = csrfsave_data()
    # # if csrfsave_data:
    token = js_encrypt(csrfsave_data())
    print(token)
    headers['token'] = token
    data = {
        # 'backUrl': '',
        'loginNo': js_encrypt('13538650881'),
        'loginPwd': js_encrypt('13538650881'),
        'code': code(),
        'requestUUID': '06357b79-787b-4253-a495-4bfdbd0aa735', # 这个参数没有校验，下面也有生成函数
        # 'guoBanAuthCode': '',
    }
    print(data)
    response = requests.post('https://login.hnzwfw.gov.cn/tacs-uc/naturalMan/loginNo', cookies=cookies,headers=headers,data=data)
    print(response.text)


def csrfsave_data():
    res = requests.post('https://login.hnzwfw.gov.cn/tacs-uc/naturalMan/csrfSave', cookies=cookies,headers=headers).json()
    msg = res['msg']
    if msg == '请求成功':
        data = res['data']
    else:
        print(msg)
        data = ''
    return data

def js_encrypt(pwd):
    with open("encrypt.js", encoding="utf-8") as f:
        js = execjs.compile(f.read(),cwd="C:/Users/thouger/AppData/Roaming/npm/node_modules")

    data = js.call("encrypt",pwd)
    return data



def code():
    url = 'https://login.hnzwfw.gov.cn/tacs-uc/login/verCode'
    token = js_encrypt(csrfsave_data())
    headers['token'] = token
    res = requests.post(url, cookies=cookies, headers=headers,).json()
    print(res)
    code = res['data']
    return code


def uuid(): # uuid生成方法一
    url = 'https://login.hnzwfw.gov.cn/tacs-uc/naturalMan/uploadIdentifier'
    token = js_encrypt(csrfsave_data())
    headers['token'] = token
    res = requests.post(url, cookies=cookies, headers=headers,).json()
    print(res)
    code = res['data']
    return code

 # uuid生成方法二
""" 
function uuid() {
	    var s = [];
	    var hexDigits = "0123456789abcdef";
	    for (var i = 0; i < 36; i++) {
			s[i] = hexDigits.substr(Math.floor(Math.random() * 0x10), 1);
	    }
	    s[14] = "4";  // bits 12-15 of the time_hi_and_version field to 0010
	    s[19] = hexDigits.substr((s[19] & 0x3) | 0x8, 1);  // bits 6-7 of the clock_seq_hi_and_reserved to 01
	    s[8] = s[13] = s[18] = s[23] = "-";

	    var uuid = s.join("");
	    return uuid;
}
"""



if __name__ == '__main__':
    # start_login()
    # code()
    uuid()