from hashlib import md5

def encrypt_md5(s):
    # 创建md5对象
    new_md5 = md5()
    # 这里必须用encode()函数对字符串进行编码，不然会报 TypeError: Unicode-objects must be encoded before hashing
    new_md5.update(s.encode(encoding='utf-8'))
    # 加密
    return new_md5.hexdigest()

orgcode = '011501,011502,011503,011504,011505,010301,010302,010303,010305,010306,010307,011601,011602,011603,011605,010201,010202,010203,011401,011402,011403,011404,010701,010702,010703,010704,010706,010707,010709,010710,010711,011101,011106'
page = '1'
t = '2022-01-10 16:08:52'
url_method = 'ddsy.product.query.orgcode.product.list.b2c'
url_ = f'method=ddsy.product.query.orgcode.product.list.b2c&orderTypeId=0&orgcode={orgcode}&otcMark=1,2,99&pageNo={page}&pageSize=100&plat=H5&platform=H5&shopId=-1&t={t}&v=1.0&versionName=3.2.0'

md5_str = url_method + url_

sign = encrypt_md5(md5_str)


url = f'https://product.ddky.com/product/queryOrgcodeProductListForB2C.htm?sign={sign}&{url_}'

print(url)
