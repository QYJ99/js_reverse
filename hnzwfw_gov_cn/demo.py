# -*- coding: utf-8 -*-
# @Time    : 2022/7/26 15:57
# @Author  : Cat
# @FileName: demo.py


import requests

cookies = {
    'SESSION': 'NzU0OTdjMzctMDJjOS00YzhmLThjNmItMDM5ODU4ZDk5YWZh',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9,zh-HK;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'SESSION=NzU0OTdjMzctMDJjOS00YzhmLThjNmItMDM5ODU4ZDk5YWZh',
    'Origin': 'https://login.hnzwfw.gov.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://login.hnzwfw.gov.cn/tacs-uc/login/index',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'token': 'XzHBSeXmYMjRyXJLLkyjG5jKlyNrf7IY8aWx2zL3MRmZNSSju76E8db3lPI0tKewFCHhJBih1G9pvFdLUc/ds+i/juxXR35ptKWO3x6GjGXFfrVuy3UH8cTam60RSLBBS2qjEJ4v1YW1tQ0ruQSi5J96TVtzJWaQdTViFKED627+nwoemdbd0NYar4mox6aApLd+QFKvWo6ALDt4aIYFdMIV8UEw2ZrJ/s24ura7rc3fXWJx6nBDbidiDp0DiO2FhNMl9uXdcn/ieP707yAwEELjYpNlpZDYIscu5WBfnGvnerN2gUKJ4nHbDq5wuWBr2ovTvpxkUgiMTOaKjFEPoA==',
}

data = {
    # 'backUrl': '',
    'loginNo': 'M/ZeKb9idrP2MqMhbKB1TUROagQFKWBociY0E/LkCHTiCi5icTuWRn1CyKC/OPWUXWVO1pPxAoGV6e1+Ln+H52+9+W645DBBlgmxElWeN5Wy91fJzNHuE4EtBBXORxpSwRnbdC28l+/XypWKvaVDJeb//63x0yu0r18L+Gx0R7EAaTUL8qeIjHkyBfP/pyAMkhVe/vKEFwBscOdph2YJOZ0yr0ffbiGEs+MPRMbQEq+vFaDpcTV+xBmv0rLrdI9OAsx/3Zn+5ThLgjECyW3VO4EGZRjPpUubk/ML0+89e044F1dxcyxY8JT2VifFrOETynZ5pPnhLlYh/rBvH3hn4Q==',
    'loginPwd': 'CbmQhAafVCHKlX5zi4ZS9YQA7CyriHo8Bc/XF/qf3DuLLwqKpcgFbRr4guN0guJgwMiBRtF/yV+4gq5OlW3KLG79CIfqa0sSB5f8hS6J5rohIPfqd9bIotjZI4zpRsvUqJ5vw/j5a75EWZih7zZy3Bd5ZyYU2R40vWHk7bfFhwycP5xM9K0bIFju+LpOxoUt0aB2qR9WOfdcnx4vRT7ZFHWCFQgYoXF0At3B08mXyr9amyhmIzU7ujENsnfazVGeSmzEV3NpU1EKpMEAUVy3mk6wo+RvPKYG4f2o1cfnB928v2HPHAxpX3pHLTxO+RRv01i0QWobwrKDaIB0COJbxw==',
    'code': '04a8df15-497f-49bd-9f12-65ae415ed563',
    'requestUUID': '06357b79-787b-4253-a495-4bfdbd0aa735',
    # 'guoBanAuthCode': '',
}

response = requests.post('https://login.hnzwfw.gov.cn/tacs-uc/naturalMan/loginNo', cookies=cookies, headers=headers, data=data)


# SESSION 访问首页拿 Cookie中的SESSION值
# token 请求https://login.hnzwfw.gov.cn/tacs-uc/naturalMan/csrfSave，然后RSA加密得到 token
# loginNo、loginPwd 账号、密码 RSA加密得到
# code https://login.hnzwfw.gov.cn/tacs-uc/login/verCode获取
# requestUUID /naturalMan/uploadIdentifier 获取 或者从js加密也可以获取



