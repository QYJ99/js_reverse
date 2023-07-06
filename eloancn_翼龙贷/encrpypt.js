const CryptoJS = require('crypto-js');  //引用AES源码js

const key = CryptoJS.enc.Utf8.parse("jo8j9wGw%6HbxfFn");  //十六位十六进制数作为密钥
const iv = CryptoJS.enc.Utf8.parse('0123456789ABCDEF');   //十六位十六进制数作为密钥偏移量


//AES ECB加密方法 t:word,e:DESkey
function AesEncrypt_ECB(t, e) {
    var a = CryptoJS.enc.Utf8.parse(e);
    var s = CryptoJS.DES.encrypt(String(t), a, {
    mode: CryptoJS.mode.ECB,
    padding: CryptoJS.pad.Pkcs7
    })
    return s.toString()
}

