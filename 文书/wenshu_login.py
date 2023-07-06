# -*- coding: utf-8 -*-
# @Time    : 2023/2/14 15:37
# @Author  : Cat
# @FileName: wenshu_login.py


import requests
sess = requests.Session()
headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        # 'Content-Length': '0',
        # 'Cookie': 'HM4hUBT0dDOn443S=xjHPRtirDtOt36tajpxsxYajKgtgs5Ku_RJZaLwBkRHmQvFyjFKUa7q3amgJAIGm; HM4hUBT0dDOn443T=4dTkERNpiNpT1aFgWHQnLb7OpUd0ZH._qUhiEnLQGG20Srm4acBTiGgGflyxkent4ZsoXJkAG3XS9jblS8cmDRYfBEd7ZbMaiXAWZc_Jo3cFUBuhNPCK0g3n_UbLKG5eX8p_14HDC7CN0RzNpYRFl_anYRWgT30VI4XAGWWBvdRLiYxNyDGZs0x5lMXyu87L1PbH7n0nV4.j7sBxec7q8b8RiLtrLuQ.eOHaZuYeSYfqzsZh9r0D61mtZoq.N_JwDsJ.44BzR0OszZ6qlj1_CZoseFfeBBrcpDUJcUI2dZ2dGiyzLn82sL_3L3NfenInBuVA; SESSION=1a5ce1a9-9a98-4580-a765-4c5c379ee71f; wzws_sessionid=gjZmNjkwMYE2MThmMzaAMTEzLjEwMy4yMS4xMDCgY+s0ig==',
        'Origin': 'https://wenshu.court.gov.cn',
        'Referer': 'https://wenshu.court.gov.cn/website/wenshu/181010CARHS5BS3C/index.html?open=login',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

def authorize():

    response = sess.post('https://wenshu.court.gov.cn/tongyiLogin/authorize', headers=headers)
    print(response.text)
    print(response.cookies.items())

def login():
    data = {
        'username': '135888880881',
        'password': '', # 加密方式在 ./get_enc_passwd.js
        'appDomain': 'wenshu.court.gov.cn',
    }

    response = sess.post('https://account.court.gov.cn/api/login', headers=headers, data=data)
    print(response.text)
    print(response.cookies.items())


def get_session():
    url = 'https://account.court.gov.cn/oauth/authorize?response_type=code&client_id=zgcpwsw&redirect_uri=https%3A%2F%2Fwenshu.court.gov.cn%2FCallBackController%2FauthorizeCallBack&state=d33d394e-30b3-438b-a951-d14cb7dc7810&timestamp=1676363292370&signature=9186D4A740CD076CF9C716C15740226FCC921D31E56B50CE0E6E88DD074708AA&scope=userinfo'
    cookies = {'SESSION':'09e2e5f98-8646-4a66-95a4-3946ff8b2272' , 'HOLDONKEY':'YjdjNzZlYzEtNWU4YS00MDRmLTliMzktMzFjMzNlNDcyMzcz'}
    response = sess.get(url, headers=headers,cookies=cookies,)
    print(response.text)
    # print(response.headers['Location'])
    print(response.cookies.items())
    url = 'https://wenshu.court.gov.cn/website/wenshu/181029CR4M5A62CH/index.html?'

    resp_07 = sess.get(url=url, headers=headers)
    print(resp_07)
    print(resp_07.cookies.items())
    return resp_07.cookies.items()


authorize()
login()
