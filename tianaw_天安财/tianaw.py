# -*- coding: utf-8 -*-
# @Time    : 2022/1/10 18:18
# @Author  : Cat
# @FileName: tianaw.py

import json
import requests
import execjs


with open("./encrpypt.js","r", encoding="utf-8") as f:
    js_code = f.read()
ctx = execjs.compile(js_code)

# 加密
data = {
    "body":{"loginMethod": "1", "name": "13588880998", "password": "gfhgjgrtg"},
    "head":{"channelCode": "101","customerId": "","transSerialNumber": "","transTime": "1641809292016","transToken": "","userCode": ""
        }
}
d = json.dumps(data)
print(d)
jsonKey = ctx.call("oo",d)
# jsonKey =jsonKey.replace('"','')
print(jsonKey)


# 解密
aa_data = "gGT9N2pHEZZTlK2B6XzGN44O/vXk4JTRV2eLqfUCoTwuiQwjQCN4JHN3EZ5FT08uRRh1efcVDhir\nDNjggE3HYtthhHKNt3ePQC4QtIvcF/xhRxSVnTN0soLR1BG6wr+xLq6+bKrqCKT2ZtX8QioLreIN\nah9UH/yF3e6GxNWMEe2ElhRA6qaVE2WNBaKrBVUjX3cqgXIUNqYqEvP9XLclehrPRbObJEi4g5f1\njiDn8NF/oiue5P1chFi6Xfkd4ayJbD6Q7TdUqb4HzfefsxNaKhmPNRG5wDapURsVctcm90A="
aa_res = ctx.call("aa",aa_data)
print(aa_res)



