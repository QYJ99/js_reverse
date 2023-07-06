const  MD5 = require("crypto-js");

function get_sign():
    y = 'ddsy.product.query.orgcode.product.list.b2cmethodddsy.product.query.orgcode.product.list.b2corderTypeId0orgcode010101,010104otcMark1,2,99pageNo1pageSize100platH5platformH5shopId-1t2021-12-3 18:36:2v1.0versionName3.2.06C57AB91A1308E26B797F4CD382AC79D'
    v= MD5(y)
    e = "https://product.ddky.com/product/queryOrgcodeProductListForB2C.htm"
    l = [
        "method",
        "orderTypeId",
        "orgcode",
        "otcMark",
        "pageNo",
        "pageSize",
        "plat",
        "platform",
        "shopId",
        "t",
        "v",
        "versionName"
    ]

    for (var y, v , k = e + "?sign=" + v, w = 0; w < l.length; w++)
        (t.get(l[w]) + "").indexOf("+") >= 0 || -1 != (t.get(l[w]) + "").indexOf("&") ? k += "&" + l[w] + "=" + encodeURIComponent(t.get(l[w])) : "pageUrl" == l[w] ? k += "&" + l[w] + "=" + encodeURIComponent(t.get(l[w])) : k += "&" + l[w] + "=" + t.get(l[w]);
    return k