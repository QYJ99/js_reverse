
# @Time    : 2022/7/27 14:03
# @Author  : Cat
# @FileName: demo_jszc_mohurd.py

# 解决：execjs UnicodeDecodeError: 'gbk' codec can't decode byte
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")
# 参考 https://blog.csdn.net/qq_39799322/article/details/124188879


import requests
import execjs

cookies = {
    'Hm_lvt_b1b4b9ea61b6f1627192160766a9c55c': '1658890011',
    'Hm_lpvt_b1b4b9ea61b6f1627192160766a9c55c': '1658891383',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,zh-HK;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'Hm_lvt_b1b4b9ea61b6f1627192160766a9c55c=1658890011; Hm_lpvt_b1b4b9ea61b6f1627192160766a9c55c=1658891383',
    'Pragma': 'no-cache',
    'Referer': 'https://jzsc.mohurd.gov.cn/data/company',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'timeout': '30000',
}

params = {
    'pg': '1',
    'pgsz': '15',
    'total': '450',
}

res = requests.get('https://jzsc.mohurd.gov.cn/api/webApi/dataservice/query/comp/list', params=params, cookies=cookies, headers=headers).text


with open("./encrpypt.js","r", encoding="utf-8") as f:  # spiders/module/
    js_code = f.read()
ctx = execjs.compile(js_code,cwd=r"C:\Users\thouger\AppData\Roaming\npm\node_modules")
result = ctx.call("h",res)
print(result)

