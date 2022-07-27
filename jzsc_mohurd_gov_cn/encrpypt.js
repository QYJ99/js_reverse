const CryptoJS = require('crypto-js');


function h(t) {
    var e = CryptoJS.enc.Hex.parse(t)
      , n = CryptoJS.enc.Base64.stringify(e)
//    var n = CryptoJS.enc.Base64.parse(t).toString(CryptoJS.enc.Utf8)
      ,f = CryptoJS.enc.Utf8.parse("jo8j9wGw%6HbxfFn")
      , a = CryptoJS.AES.decrypt(n, f, {
        iv: CryptoJS.enc.Utf8.parse("0123456789ABCDEF"),
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    })

      , r = a.toString(CryptoJS.enc.Utf8);
    return r
}

const key = CryptoJS.enc.Utf8.parse("jo8j9wGw%6HbxfFn");  //十六位十六进制数作为密钥
const iv = CryptoJS.enc.Utf8.parse('0123456789ABCDEF');   //十六位十六进制数作为密钥偏移量

//AES解密方法
function AesDecrypt(word) {
    let encryptedHexStr = CryptoJS.enc.Hex.parse(word);
    let srcs = CryptoJS.enc.Base64.stringify(encryptedHexStr);
    let decrypt = CryptoJS.AES.decrypt(srcs, key, { iv: iv, mode: CryptoJS.mode.CBC, padding: CryptoJS.pad.Pkcs7 });
    let decryptedStr = decrypt.toString(CryptoJS.enc.Utf8);
    return decryptedStr.toString();
}
