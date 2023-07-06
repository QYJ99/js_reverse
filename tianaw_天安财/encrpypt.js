const CryptoJS = require('crypto-js');  //引用AES源码js

function oo(l){
    var n = "y2EGNpHk35C8MKKx"
      , t = "y2EGNpHk35C8MKKx"
      , e = CryptoJS.enc.Utf8.parse(l)
      , a = CryptoJS.AES.encrypt(e, n, {
        iv: t,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    });
    res = CryptoJS.enc.Base64.stringify(a.ciphertext)

    return JSON.stringify(res)
            }


function aa(l){
    var n = CryptoJS.enc.Base64.parse(l)
      , t = "y2EGNpHk35C8MKKx"
      , e = "y2EGNpHk35C8MKKx"
      , a = CryptoJS.lib.CipherParams.create({
        ciphertext: n
    });
    var decrypted =  CryptoJS.AES.decrypt(a, t, {
        iv: e,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    })
    var plaintext = decrypted.toString(CryptoJS.enc.Utf8);
    return plaintext;
  }


//aa_data = "Da47+ABqNgUEPX63erFY1qjLfpy0hEzZWwnzfM11SLO3s5dKl73r91aM+vHDbOtWUd01/5zg2PhwvJvCeqmQCABxvHI0GCcFoUSsvFDHy4mJzk/VYR67XBOHukyOYAXR7GecXi/rYO/VByAexnG7xMbtfDpu3YVAlTF6bb96P99NWvR+TpgcZcHv0gLxtNslXRavsiKU96RUq/qjVyud1DZuYbCd2LGvS1PTjURi2/cZ5cJ6pd6NP9LDeDnobRizqjRm0C4yk8WysizT8eeuJKJ64u78ZLa/6rRKI59DPPo="
//
//
//
//dd = aa(aa_data)
//console.log(dd)