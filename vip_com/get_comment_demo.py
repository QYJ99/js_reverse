# -*- coding: utf-8 -*-
# @Time    : 2022/7/26 18:12
# @Author  : Cat
# @FileName: get_comment_demo.py


import requests

cookies = {
    'mars_pid': '0',
    'vip_address': '%257B%2522pid%2522%253A%2522104104%2522%252C%2522cid%2522%253A%2522104104101%2522%252C%2522pname%2522%253A%2522%255Cu5e7f%255Cu4e1c%255Cu7701%2522%252C%2522cname%2522%253A%2522%255Cu5e7f%255Cu5dde%255Cu5e02%2522%257D',
    'vip_province': '104104',
    'vip_province_name': '%E5%B9%BF%E4%B8%9C%E7%9C%81',
    'vip_city_name': '%E5%B9%BF%E5%B7%9E%E5%B8%82',
    'vip_city_code': '104104101',
    'vip_wh': 'VIP_NH',
    'PHPSESSID': 'b9nicih27jbmqls4cpu5ibbho7',
    'mars_sid': 'eda46cb78ce4945f601f8092c3494631',
    'vc_token': 'eyJ0b2tlbiI6Ijk0NzdmMjBmNTFlMTYzZDQyYTBhMTM2YWY3ZDBiY2RjIiwidG9rZW4xIjoiYmU2YzM0OTIwMDBkYjQ3NDVkNzA3NDI0ZTEzMWQ4OGYiLCJ2ZW5kb3JJZCI6IjIyMDUiLCJ1c2VyTmFtZSI6ImFsaWNlLnpoYW9AaTJtYWdvLmNvbSIsInZlbmRvckNvZGUiOiIxMDUyMDkiLCJ1c2VySWQiOiIxNTY0NjMiLCJ2aXNTZXNzaW9uSWQiOiJiOW5pY2loMjdqYm1xbHM0Y3B1NWliYmhvNyIsImFwcE5hbWUiOiJ2aXNQQyIsInZpc2l0RnJvbSI6InZjIn0%3D',
    'mars_cid': '1652928072766_3752d973b2f981da0a91489b09080282',
    'visit_id': '4E57595B152A9675E57E5A377FF0F80A',
    'user_class': 'a',
    'VipUINFO': 'luc%3Aa%7Csuc%3Aa%7Cbct%3Ac_new%7Chct%3Ac_new%7Cbdts%3A0%7Cbcts%3A0%7Ckfts%3A0%7Cc10%3A0%7Crcabt%3A0%7Cp2%3A0%7Cp3%3A1%7Cp4%3A0%7Cp5%3A0%7Cul%3A3105',
    'vip_access_times': '%7B%22detail%22%3A1%2C%22list%22%3A2%7D',
    'vip_tracker_source_from': '',
    'VipDFT': '0',
    'pg_session_no': '2',
    'VIP_QR_FIRST': '1',
}

headers = {
    'authority': 'mapi.vip.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,zh-HK;q=0.8',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'referer': 'https://detail.vip.com/',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}

params = {
    'callback': 'getCommentDataCb',
    'app_name': 'shop_pc',
    'app_version': '4.0',
    'warehouse': 'VIP_NH',
    'fdc_area_id': '104104101',
    'client': 'pc',
    'mobile_platform': '1',
    'province_id': '104104',
    'api_key': '70f71280d5d547b2a7bb370a529aeea1',
    'user_id': '',
    'mars_cid': '1652928072766_3752d973b2f981da0a91489b09080282',
    'wap_consumer': 'a',
    'spuId': '1472753881100443648',
    'brandId': '1710613408',
    'page': '10',
    'pageSize': '10',
    'functions': 'angle',
    'timestamp': '1658830282000',
    'keyWordNlp': '全部-按默认排序',
    '_': '1658830222516',
}

response = requests.get('https://mapi.vip.com/vips-mobile/rest/content/reputation/queryBySpuId_for_pc', params=params, cookies=cookies, headers=headers)
print(response.text)