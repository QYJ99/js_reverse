import execjs


with open("./encrpypt.js","r", encoding="utf-8") as f:
    js_code = f.read()
ctx = execjs.compile(js_code)
data = '1234567890'
DESkey = "e9284d45-cf2a-4e46-9367-f122413ca6b0"
res = ctx.call("AesEncrypt_ECB",data,DESkey)
print(res)