# -*- coding: utf-8 -*-
# @Time    : 2022/8/16 19:45
# @Author  : Cat
# @FileName: get_sign.py


import requests
import hashlib

def get_info():
    headers = {
        'Host': 'app.dewu.com',
        'Connection': 'keep-alive',
        'AppId': 'wxapp',
        'SK': '换成自己抓包的数据',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
        'appVersion': '4.4.0',
        'content-type': 'application/json',
        'platform': 'h5',
        'wxapp-route-id': '[object Undefined]',
        'Referer': 'https://servicewechat.com/wx3c12cdd0ae8b1a7b/340/page-frame.html',
    }
    data = {"tabId":"","limit":20,"lastId":3,"platform":"h5","version":"4.73.0","isVisitor":"false","newAdvForH5":"true"}
    sign = get_sign(data)
    data["sign"] = sign
    print(data)
    response = requests.post('https://app.dewu.com/api/v1/h5/index/fire/index', headers=headers, verify=False,json=data)
    print(response.text)


def get_sign(data):
    data_str = ''
    for i in sorted(data):
        data_str += i + str(data[i])
    print(data_str)
    res = data_str + "反编译js中找到"
    h1 = hashlib.md5()
    h1.update(res.encode(encoding='utf-8'))
    sign = h1.hexdigest()
    return sign


get_info()


