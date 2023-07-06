# -*- coding: utf-8 -*-
# @Time    : 2023/2/14 15:57
# @Author  : Cat
# @FileName: keyword_search.py

import json
import requests
import execjs

cookies = {
    'wzws_sessionid': 'gjZmNjkwMYAxMTMuNjguMjI1LjExOKBkCDXXgTJjZTFmZA==',
    'SESSION': 'cf145c65-58aa-41cf-a326-99831542cd44',
    '__utma': '61363882.707099459.1678273158.1678273158.1678273158.1',
    '__utmc': '61363882',
    '__utmz': '61363882.1678273158.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9,zh-HK;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'wzws_sessionid=gjZmNjkwMYAxMTMuNjguMjI1LjExOKBkCDXXgTJjZTFmZA==; SESSION=cf145c65-58aa-41cf-a326-99831542cd44; __utma=61363882.707099459.1678273158.1678273158.1678273158.1; __utmc=61363882; __utmz=61363882.1678273158.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'Origin': 'https://wenshu.court.gov.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://wenshu.court.gov.cn/website/wenshu/181217BMTKHNT2W0/index.html?pageId=7a7a1dcdb98f9b0964a4f03a079b9294&s8=02',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'pageId': '7a7a1dcdb98f9b0964a4f03a079b9294',
    's8': '02',
    'sortFields': 's50:desc',
    'ciphertext': '1110001 1100101 1000100 1001111 1111010 1000110 1011010 1011001 1001110 1011000 1101010 110001 110001 1100101 1011000 110101 111001 1010001 110011 110000 1111000 1000001 1110101 1110010 110010 110000 110010 110011 110000 110011 110000 111001 1001000 110100 1110010 1001110 1001000 1001000 1001101 1011000 110010 110001 1000110 1010010 1100101 1000101 1001111 110001 1011001 110101 1000010 1100101 1001011 1000001 111101 111101',
    'pageNum': '6',
    'pageSize': '5',
    'queryCondition': '[{"key":"s8","value":"02"}]',
    'cfg': 'com.lawyee.judge.dc.parse.dto.SearchDataDsoDTO@queryDoc',
    '__RequestVerificationToken': '5TAtrGBKF2JEjskrDbQkLvbL',
    'wh': '937',
    'ww': '1920',
    'cs': '0',
}

res = requests.post('https://wenshu.court.gov.cn/website/parse/rest.q4w', cookies=cookies, headers=headers, data=data).json()
# print(res.text)

secretKey = res['secretKey']
result = res['result']


with open('decrypt.js', 'r', encoding='UTF-8') as f:
    js_code = f.read()
context = execjs.compile(js_code)
resultStr = context.call("decrypt", result, secretKey)
result_json = json.loads(resultStr)['queryResult']
print(result_json)





