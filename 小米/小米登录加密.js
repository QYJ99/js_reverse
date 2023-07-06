
const JSEncrypt = require('JSEncrypt');
const CryptoJS = require('crypto-js');

// const keyWordArray = CryptoJS.enc.Utf8.parse(key);
// const ivWordArray = CryptoJS.enc.Utf8.parse(iv);

function It(t) {
    var e;
    t = t || {};
    var i = function(t) {
        // 生成一个包含指定长度的随机字符串
        var e = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*";
        var i = "";
        for (var r = 0; r < t; r++) {
            var n = Math.floor(Math.random() * e.length);
            i += e.substring(n, n + 1);
        }
        return i;
    }(16);

    // 创建一个新的 RSA 实例
    var r = new JSEncrypt();
    // 设置 RSA 的公钥
    r.setPublicKey("MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCYEVrK/4Mahiv0pUJgTybx4J9P5dUT/Y0PuwMbk+gMU+jrZnBiXGv6/hCH1avIhoBcE535F8nJQQN3UavZdFkYidsoXuEnat3+eVTp3FslyhRwIBDF09v4vDhRtxFOT+R7uH7h/mzmyA2/+lfIMWGIrffXprYizbV76+YQKhoqFQIDAQAB");
    // 使用 RSA 公钥加密随机字符串
    // var s = r.encrypt(window.btoa(i));
    var s =  r.encrypt(Buffer.from(i).toString('base64'));

    var h = CryptoJS.enc.Utf8.parse("0102030405060708"); // 创建一个 16 字节的初始向量
    var u = CryptoJS.enc.Utf8.parse(i); // 将随机字符串转换为字节数组
    // var f = window.btoa(n()(t).join(",")); // 将对象 t 中的属性值转换为数组并编码为 Base64 字符串
    // var f = window.btoa();
    var f = Buffer.from('user').toString('base64');

    var p = {}; // 存储加密后的参数

    // 遍历对象 t 的属性
    ['user'].forEach(function(e) {
        var i = t[e];
        // 使用 AES 加密属性值
        var r = CryptoJS.AES.encrypt(i, u, {
            iv: h,
            padding: CryptoJS.pad["Pkcs7"]
        });
        r = r.toString();
        p[e] = r; // 将加密后的值存储到 p 对象中
    });

    // console.log(p)

    // 返回加密后的结果
    return {
        EUI: s + "." + 'dXNlcg==', // 对 s 和 f 进行拼接和编码处理
        encryptedParams: p // 加密后的参数对象
    };
}


t = {"user":"135xxxx0881"}
res = It(t)
console.log(res)

