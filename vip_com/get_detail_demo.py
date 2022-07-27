# -*- coding: utf-8 -*-
# @Time    : 2022/7/26 18:12
# @Author  : Cat
# @FileName: get_detail_demo.py

# 唯品会之前是有加密的，现在居然没加密了，良心啊！！！！

import requests

cookies = {
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
    'VipDFT': '0',
    'VIP_QR_FIRST': '1',
    'vipshop_passport_src': 'https%3A%2F%2Forder.vip.com%2Forder%2Forderlist',
    '_jzqco': '%7C%7C%7C%7C%7C1.224248200.1658830420104.1658830420104.1658830420104.1658830420104.1658830420104.0.0.0.1.1',
    'vpc_uinfo': 'fr713:0,fr674:D1,fr1051:0,fr766:0,fr259:S0-4,fr896:0,fr0901:0,fr884:0,fr863:0,fr392:310505,fr398:0,fr408:0,fr251:A,fr1195:0,fr344:0,fr444:A,fr848:0,fr1196:0,fr249:A1,fr328:3105,fr902:0,fr901:0,fr980:0',
    'mst_area_code': '104104101',
    'vip_tracker_source_from': '',
    'vip_access_times': '%7B%22detail%22%3A2%2C%22list%22%3A2%7D',
    'pg_session_no': '9',
    'mars_pid': '15',
}

headers = {
    'authority': 'mapi.vip.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9,zh-HK;q=0.8',
    'authorization': 'OAuth api_sign=73808aa6e39ef4751e617d3f50ecf4f09b8d6087',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'vip_address=%257B%2522pid%2522%253A%2522104104%2522%252C%2522cid%2522%253A%2522104104101%2522%252C%2522pname%2522%253A%2522%255Cu5e7f%255Cu4e1c%255Cu7701%2522%252C%2522cname%2522%253A%2522%255Cu5e7f%255Cu5dde%255Cu5e02%2522%257D; vip_province=104104; vip_province_name=%E5%B9%BF%E4%B8%9C%E7%9C%81; vip_city_name=%E5%B9%BF%E5%B7%9E%E5%B8%82; vip_city_code=104104101; vip_wh=VIP_NH; PHPSESSID=b9nicih27jbmqls4cpu5ibbho7; mars_sid=eda46cb78ce4945f601f8092c3494631; vc_token=eyJ0b2tlbiI6Ijk0NzdmMjBmNTFlMTYzZDQyYTBhMTM2YWY3ZDBiY2RjIiwidG9rZW4xIjoiYmU2YzM0OTIwMDBkYjQ3NDVkNzA3NDI0ZTEzMWQ4OGYiLCJ2ZW5kb3JJZCI6IjIyMDUiLCJ1c2VyTmFtZSI6ImFsaWNlLnpoYW9AaTJtYWdvLmNvbSIsInZlbmRvckNvZGUiOiIxMDUyMDkiLCJ1c2VySWQiOiIxNTY0NjMiLCJ2aXNTZXNzaW9uSWQiOiJiOW5pY2loMjdqYm1xbHM0Y3B1NWliYmhvNyIsImFwcE5hbWUiOiJ2aXNQQyIsInZpc2l0RnJvbSI6InZjIn0%3D; mars_cid=1652928072766_3752d973b2f981da0a91489b09080282; visit_id=4E57595B152A9675E57E5A377FF0F80A; user_class=a; VipUINFO=luc%3Aa%7Csuc%3Aa%7Cbct%3Ac_new%7Chct%3Ac_new%7Cbdts%3A0%7Cbcts%3A0%7Ckfts%3A0%7Cc10%3A0%7Crcabt%3A0%7Cp2%3A0%7Cp3%3A1%7Cp4%3A0%7Cp5%3A0%7Cul%3A3105; VipDFT=0; VIP_QR_FIRST=1; vipshop_passport_src=https%3A%2F%2Forder.vip.com%2Forder%2Forderlist; _jzqco=%7C%7C%7C%7C%7C1.224248200.1658830420104.1658830420104.1658830420104.1658830420104.1658830420104.0.0.0.1.1; vpc_uinfo=fr713:0,fr674:D1,fr1051:0,fr766:0,fr259:S0-4,fr896:0,fr0901:0,fr884:0,fr863:0,fr392:310505,fr398:0,fr408:0,fr251:A,fr1195:0,fr344:0,fr444:A,fr848:0,fr1196:0,fr249:A1,fr328:3105,fr902:0,fr901:0,fr980:0; mst_area_code=104104101; vip_tracker_source_from=; vip_access_times=%7B%22detail%22%3A2%2C%22list%22%3A2%7D; pg_session_no=9; mars_pid=15',
    'origin': 'https://detail.vip.com',
    'pragma': 'no-cache',
    'referer': 'https://detail.vip.com/',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'app_name': 'shop_pc',
    'app_version': '4.0',
    'warehouse': 'VIP_NH',
    'fdc_area_id': '104104101',
    'client': 'pc',
    'mobile_platform': '1',
    'province_id': '104104',
    'api_key': '70f71280d5d547b2a7bb370a529aeea1',
    'user_id': '',
    'mars_cid': '1652928072766_6919320398435334472',
    'wap_consumer': 'a',
    'scene': 'detail',
    'productId': '6919320398435334472',
    'opts': 'priceView:13;quotaInfo:1;restrictTips:1;panelView:3;foreShowActive:1;invisible:1;floatingView:1;announcement:1;svipView:2;showSingleColor:1;svipPriceMode:1;promotionTips:6;foldTips:3;formula:1;extraDetailImages:1;shortVideo:1;countryFlagStyle:1;saleServiceList:1;storeInfo:1;brandCountry:1;freightTips:3',
}

response = requests.post('https://mapi.vip.com/vips-mobile/rest/shopping/pc/detail/main/v6', cookies=cookies, headers=headers, data=data)
print(response.text)