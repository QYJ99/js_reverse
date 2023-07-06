import json
import execjs
import requests
keyword = 'cat'

def get_sign(keyword):
    with open('./sign_js.js',encoding='utf-8') as f:
        js_code = f.read()

    sign = execjs.compile(js_code).call('e',keyword)
    # print(sign)
    return sign

sign = get_sign(keyword)
print(sign)

headers = {
    'Host': 'fanyi.baidu.com',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Cookie': 'BIDUPSID=EE37CCD96820499573960379D3EDD2AC; PSTM=1624503351; BAIDUID=EE37CCD968204995E7957376B6A300A6:FG=1; __yjs_duid=1_a56c2d791a03142b071eb9534019f26b1624506188544; BAIDUID_BFESS=B6B623B1D12CC1D48741E4055A52DB7D:FG=1; BAIDU_WISE_UID=wapp_1635734528326_404; ZD_ENTRY=google; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; __yjs_st=2_ZjY1MTk3MTljZjA2OTQzMGNkMTMzMDhmOWU2ZGMxNzZlZTg5NzQ5YTljOWU5MTM0ZTE4MjBiYWRmZWMyMDU2OTdhYjFiYWUwMmNlNWYwZTlmYmY2NGM3M2NiMzVmMzg3ZTczYjZiNjE4MjQ2N2ExODVlMDBkN2VjZTQ4Yzk0MTg0YTBhNzMyNDI1OTAyZjI0OWNhODcyOTM3OGIyNGRiNTU2YmM3ODkzODY0YzAxZTY5YTZjMjA0ZDVkMzA5NTVmNzMxY2ZiNjQ4YWYxOGNhNDgyMWEyNzgzZTRmZjY1YzM2ZDdlNTAwMDIwZTk0NjI1Y2U3ZGYzZGQwYzg1MTk0ZV83Xzc3ZThhNjc5; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1637311837,1637311937,1637315660,1637315691; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1637315691; ab_sr=1.0.1_OGIyMDRmZDRlMzE0M2JmOTc0NDI4NjY3NTE2MWNjZTUzMzc1MTQ4ZDVlYzEwMzQwMGQ1MzJmNzE0ZTlmNTMyYzkyZjdhM2IwZTJkN2NkNzY5MGNmNDAwZWViNTUyNDMzYmM1YTA0NTM4Y2NkNWVjMWQ5YThjZGUxMDhhY2IzNWJhZWMxYzFlNGFkZDIzNTc2NzkxNzQ1OGE5YmVjYTY1Mw=='
}

data = {
    'from': 'en',
    'to': 'zh',
    'query': keyword,
    'simple_means_flag': '3',
    'sign': sign,
    'token': 'd6819cdf12a44e6a6a13d19123260955',
    'domain': 'common',
}

url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

res = requests.post(url,headers=headers,data=data)

d = json.loads(res.text)
print(d)

