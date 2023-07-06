
// -----------------------------------     hash加密     -------------------------------------------------

 const crypto = require('crypto');

 function encryptHash(data, algorithm) {
   const hash = crypto.createHash(algorithm);
   hash.update(data);
   return hash.digest('hex');
 }

 const data = 'Hello World!';
 console.log('MD5:', encryptHash(data, 'md5'));
 console.log('SHA1:', encryptHash(data, 'sha1'));
 console.log('SHA256:', encryptHash(data, 'sha256'));
 console.log('SHA512:', encryptHash(data, 'sha512'));


 -----------------------------------     AES加密（crypto）     -------------------------------------------------

 使用crypto
 const crypto = require('crypto');
 // AES加密
 function encryptAES(data, key, iv, algorithm) {
     /*
     data : 待加密/解密的数据,
     key : 密钥,
     iv : 初始化向量（IV）,
     algorithm : 和加密模式
     */
     const cipher = crypto.createCipheriv(algorithm, key, iv);
     let encrypted = cipher.update(data, 'utf8', 'hex');
     encrypted += cipher.final('hex');
     return encrypted;
 }

 // AES解密
 function decryptAES(data, key, iv, algorithm) {
      /*
     data : 待加密/解密的数据,
     key : 密钥,
     iv : 初始化向量（IV）,
     algorithm : 和加密模式
     */
     const decipher = crypto.createDecipheriv(algorithm, key, iv);
     let decrypted = decipher.update(data, 'hex', 'utf8');
     decrypted += decipher.final('utf8');
     return decrypted;
 }

 const data = 'Hello World!';
 const key = '0123456789abcdef0123456789abcdef';
 const iv = '0123456789abcdef';
 const algorithm = 'aes-256-cbc';
 const encrypted = encryptAES(data, key, iv, algorithm);
 console.log('Encrypted:', encrypted);

 const decrypted = decryptAES(encrypted, key, iv, algorithm);
 console.log('Decrypted:', decrypted);


// -----------------------------------     AES加密（crypto-js）     -------------------------------------------------

const CryptoJS = require('crypto-js');

// AES加密
function encryptAES(data, key, iv, mode, padding) {
    /*
    待加密的数据 data、密钥 key、初始化向量 iv、加密模式 mode 和填充方式 padding。
    其中，key 和 iv 都需要转换为 WordArray 格式，使用 CryptoJS.enc.Utf8.parse 方法实现。
    mode 和 padding 都可以通过选项对象来设置，选项对象中还包括 iv 属性
    */

  // 将密钥和IV转换为WordArray格式
  const keyWordArray = CryptoJS.enc.Utf8.parse(key);
  const ivWordArray = CryptoJS.enc.Utf8.parse(iv);

  // 使用选项对象设置加密方式、填充方式和IV
  const options = {
    mode: CryptoJS.mode[mode],
    padding: CryptoJS.pad[padding],
    iv: ivWordArray,
  };

  // 对数据进行加密
  const encrypted = CryptoJS.AES.encrypt(data, keyWordArray, options);

  // 将加密后的数据转换为Base64字符串格式
  const ciphertext = encrypted.ciphertext.toString(CryptoJS.enc.Base64);

  return ciphertext;
}

// AES解密
function decryptAES(ciphertext, key, iv, mode, padding) {
  /*
  密文 ciphertext、密钥 key、初始化向量 iv、加密模式 mode 和填充方式 padding。
  与加密函数类似，key 和 iv 都需要转换为 WordArray 格式，使用 CryptoJS.enc.Utf8.parse 方法实现。
  mode 和 padding 都可以通过选项对象来设置，选项对象中还包括 iv 属性
  */

  // 将密钥和IV转换为WordArray格式
  const keyWordArray = CryptoJS.enc.Utf8.parse(key);
  const ivWordArray = CryptoJS.enc.Utf8.parse(iv);

  // 使用选项对象设置加密方式、填充方式和IV
  const options = {
    mode: CryptoJS.mode[mode],
    padding: CryptoJS.pad[padding],
    // iv: ivWordArray,
  };

  // 将Base64字符串格式的密文转换为WordArray格式
  const ciphertextWordArray = CryptoJS.enc.Base64.parse(ciphertext);
  // 对数据进行解密
  const decrypted = CryptoJS.AES.decrypt(
    { ciphertext: ciphertextWordArray },
    keyWordArray,
    options
  );
  // 将解密后的数据转换为UTF-8字符串格式
  const plaintext = decrypted.toString(CryptoJS.enc.Utf8);
  return plaintext;
}


const data = 'hello world';
const key = 'd245a0ba8d678a61';
const iv = 'EkpTEA3FbZFGGq8Y';
const mode = 'ECB';
const padding = 'Pkcs7';

// const ciphertext = encryptAES(data, key, iv, mode, padding);
// console.log(ciphertext);

// ciphertext = 'NjU0RENCNDUyNzEwOEZBMkI2Nzg1OTc4NzVGMzE4RTAuY0dGeVlXMGZNemRqTjJVNU5XRXROakk1WkMwME56QXdMV0V3WldJdE56aGtaVFEyTVdVd1ltSmhIblpsY25OcGIyNGZNUjV3YkdGMFptOXliUjloYm1SeWIybGtIbVZqSHpFPS4kPIrO3XmffxPEbuwERYmUnN_HpTBpU45125ihsOf0bdLsA81pPWPAAxOPZvSxiIIf-yokkUW09fWtT9lMQ7KKqY5ChwksZw-03zdPRBW-Ficp-2-R2RobYdLN7kUR1NuSNP28fxM8xw=='

// ciphertext = 'VWCtCY9BuUo+Me9Kc3K09Ta4UvLyV9Lddf+m9nLfgrz0+VjXxp+Wl3UjrDx3DTdSEN4q902yr/34pH7ovZa0ouhSwTg147l0vuUnVyH6YQe3XD1m2Qv/BwQtntB6FhnxZ6CzmzjcaRO78JVLEgV/SoVd9pL1TLKw4ZCwxjl/W4LDUn0lb7J4lH6V1WNP3DbutDIhGvr8FnHwU3vz9uXZsA=='
ciphertext = "jYITj0Igyd3VbeKmcSpjo_telbL0B7s8ibTE3UVF4yAf8ysK4g7xP0_7rVewNVaxhH9Ak35rD7pdGct6_t5Ycz9Rvrlf4vQte6pa-8FgjTGuodBX4Vw5OKGkc2lazYIZv69yGg2aEQnAz60RAov82xzYAOZYdotenY40o1nXfVHLrn0nqdKgJIEpHP2sZJ0V6BgHLhtaRy2leWfwlJs6k4YdxQr5cUMyYBl52W1-LA7e4dZpgG29WAQaKcJGYQ3TIS4MA7Itv7-yjO5ZMVMxLvSXWQKkpdM-3j3IujMv7D0BuBBSP43qYdALJiZhxk4mmFLQSc65pxWmcg1OrxWMfVHgWqCm9Aj46ZIWQpeiKE2yWKy4R4dKcGKGWdt3lrQkvpFOCoQ9ixkHRhK8gt2s1ED_BZFDvFwLJBELbwLuLXCDAYpnpti_CbZ4Q4-leCmYIhGYxYkADrS07iG6x5fsbalqaWFMuxLf_w-KsOO4GfEG2qXB74XbMR7PW5JKMzzMhbqBnSl-DzmdQS31R4jjySuFxcnh8hD_78qw-O_Bq8i7otWMpEeeQ7ESi08i2S_sRp97c00tjpQysZM80tB9UB5vkRLe3EKFw7RqVl5aqe8D3BReWgtsPN_IxZwNSHuE-Y_ZCkFcBgeqKFV7b6EP43UJgB1M6V-YG9ErPFJhYxlKBLNl60Y7NiPviHwQTsUvgFBjMaV_m-Red23Lwi0JfvnnhJ1amm7Fo1oCQMaXVbKoYbWtx-BscAYhmNOIoLcoen9aZzRlxX-nNwQmVqWyqHtMMo6e_R34aIoraiCuic0kbKyLcbigJvNSLlg9_aIsgbox4TcBUCPBdwiwZ6OCkbUfR1TQngE2IKF96bcvt_ceMvkoFKLnnxe5v1ahC2UtsJ-X7H30JWuM8eDIidzfo34sTgdcnMTjMu7A1ak7b3hFLJe9TZYT4gJ55WHZ-N-3QGA4FpDA7kxywA7fhmMCrqbCsGMDELJcCpUToDPfTl1qHIrQ83QxTeCyEy9SC7To41uDc2ai32BTHjQ-z_9piWpXGhA0-Nu7yF2GbF2qzZx86FJOjmat71m6PDoZi5gQBdRinKibZ8cIRYHJlk1ayURFiYaEniMYMiibBZx05yU63lPLAOl5vOKtYATEeoY0WHQccmPwu3NZ5vMrIkjZvow1KJd_d3sINtdzpdKMCNjVnVGz1fnYNUpVu4GnbagJ_QvTkDEKd60wB0TDWhCfYnuTU_9nV6Ogulv1H4S2bTEL0-MT5UuIMIYQZ-r-Hk3wZWKemhrTtiZkmsKp4qRGAaNrj7cA0ddat1jeZfUqRjy8PtOE8sn9bhHkne9RCMv9aG9G_Q_TuuWPS-aGscSC4oY78xQyRmp6PYc9LSvNKpnRttRAAoTJ7reMtGfpqk19QhECbJuFJKj0wvjn4OghNWkPbaBLdV8u4Zlm4DjlsVIEEJO_p4XE5EyMHOZCUcGL7Fsek3xC7t04rLHt1mYleHRtDMVCAPCXoebqyMJyNThXaiWjGOyX40GBkKYqxG8wzpcHkOPiZ3Ki4ZDti10ErhttPezSNnstUa2q06yGvBrqiX4qBRb7w1bABG8YFFfBaKRGsCiebdQvfDaLv91Lu8p2SmknAyCdndrinnMxTBkBxrO5LTtjK_mNbK1WilfEqgrzIfHrBPElT9sKG5Aszffvw1QW3JNBksaD2KXC96I0lWaeIHEjlZ57zX9Rz0rHgwWuH_PEzXDZehaRHFcgQjaxheubfZNQGjAr6T7f668dneWCfUMTuFdYv0_P51OwTiYfzCk0OQk2q4TJlslFfQsRrxUzNWoNTXdkN5hvpioLMa_oCfWxwkg-KllEQbkXCDOmxW_cHCofXQnpvw_vBvBO-t14dBXzgqaX77EeqI6QWWqCPuWIX429vpT7G5Rl12VhBrtwei9gm5TUa6j2FQNdnIKdyWCOZavyJnExMqK-xJ0TmCjB2dvOfXa5TBxIf1yfUzpFK6AzsfBoj-1zadgsP1vJVdaF72iolCxIvd0X1SljiSTmYNodWrTEMu_JUscGbY5fU5Ob192i0gfWJRn3jheUawFPgcTpQtzju_OZU0VKcuVCb_ZyrYWED0hCXbQa3UWUQQ9FMMCbcrQ566DrbBs75LOqHCEz_nPDpC7JRgKFxjI2OkE-OT7hGeAuoyFXpvRGnYGbebz5sqyDBgBduGz3-uQaPTFNAcTnX-CNh41iSQnvhZKisNRnv-ACyLIc9viTk9COCqOlucBxPP5CCqlXY9I16x8Qf1MyNgJ1oW5OxN5sFeD0Fd_nTYn_Z4kPo0JeCe1YIH3U7gdXx1kxRS2CY0UOfZGdqj8O5A5CKwShuykeUIGBPIcAWF09Ngx9pDXFydqC8VjctrWpP647zjcjqZLygokNHYCYJoU8s8vhbJJWtppEnl1z-GUXxd7-Yptp1pIaIKQRhI_E7yRApu0PvdId4APim6yQdefs3av2CP1dl52rYPlfZHT2IeNqABr7YVzgfoJtI_zZDInedvzBuEL6DM8vR6cSAvQN_wsZwEWfaKMxCNrxrtP2mzwumu-dsewU5Z6MJjA3hmCsKt4x6XLEdJVVCQ5ArapybiR_KSSKoTSmj0XvtmDbmptSCyaDoHd_Ut_DmQt5JbZeUTOasSNDq6IxMirMn8wg6-kTM0QFdx-S_DiZuAb9upFn-ixTQVvw8sesHtJp8HqL5wn421QrwsD01iTjudbkolBeBSk1hDcjWYmztR8x-Gj7ngOzPnG83Z0lvkWGQ8JgyLu3kEJy9y_Ti8VnlDDwGtUsFqlnNZFF1HW3k1Sm3CcQ4gzxWDOFkVDNBvVAEdK3a91pXRfE8rqIn70bSDEoa-PW8bnfiPzIdWFaylnhfRTLsmSHs3g1UsqojxvSOs9glc0MAGFS8R7W-T-cJkFOoMqL6RzBbIPinz6sKhWsrIi1xdqEBuOqJqNmeloyEm9_VW-zoYlXTEKG-vUZpS6ekaNCxSEkaJY7zBxd1p_OxX5RUSWoRHKvt1C464i_zQT4xRe16mLZSavXBS4lWPzDhE6p06jO8QGGCnLPMhTmQBME8-4XqkBdjhUL3lS5i1tt0_KZd4lV0oqZiQ_gb_E5UxwjZ_xXRPleXTZBNETpXVbFNYkFTzKcR4t5gwbUAS-YbcZzS5f4fXY2vux0IBUk-N71op1CO8CH9a5OOGztHJrc3iU8UgKD6Ch9CVQ4GsnTFUUQIykVZ2zJ6R9X9wSbRVIETKFpNGGHMEsfIcK2dJ1DFYl5-VqqMgqZjkEHRSt4D64l4bQ0Z6DZt8G3kJlJCv4HSp2m3KfNlOAE6RbxFkesAB5srDuFZAx2EoXeAhC1KPrNAzFdOMhJ6xHifkjFteQBRs8sy4wEzdMJJTHuaCel3PcaHngjzJwh13nyD5XHWjJdjuKklBTAd68Q5QhSn3TBKTvrKpB4HiEyJDrvz2PrMeWG8lFC4vEdGRCm6cZO6hdLO78AW70uOee9KL9wcvYOPasIc54cJu7c6vkPzElVnJTFvdXFf8OPbyL_sl3umcAHak10a0NmRDzorOtTFVLajMRJ13EFRTeYLcXqWeGkrpdKY_C7t3yo-qLvlqrtfAghs-XRoAR1sSpbIL-BF5NpeiDyZpwf2B7qLPwY1chQE0UjlMCZYPvB5pmBFbEwkBQjnQoy5ZRzMJn4L6Zi2RVXNXp4j207-1clRJu4bVSnafpL59ku3lKCEJJIFGe5MRlHFQwBfPtS4QcIbeiOdfQdlSbD3th7NLIErO0I9OG4mmj48DCL3s9DqRcnBAYjLJEDwqS2mp9jf-vmdBQO6Rp5Au_8zQW4GOLfRGrUR0cgJB_GFmrF4-RRVR6Q-jfKryintEu9_nKksFjIWah0jhcApAjs20Qbe4cHmmKDuMpt1fyqDZT_GgY3woS6GVlKg530_UNeKPvw9siOm6Dsh8zxwTSRZacU282XnIf386fzcxGURI6kmzBw1_QLOlNYTrg29q7sWVrXylkeltAHwCfQ6e66t4xAEG0i6Sl1WBF09-6-RfNHSFMWDOrGCqHwmITekuYF_cO1LmrQg-hnhcRzEU2D403AqG9LjXjhWGqAV1sYRB5VQirZ_kvQ7HOx4US58sDZpiz6yL6ttX4cPixRhctd5oQKfzJ84UmRqFDC_lKZG6aNmsdtOaVQXVGWyYgUCHdzmNGcTDC9VVgru-l-hJnlPRILEYH4burARj3cM0OWyyn2S7qV8hk3vcslDobBjNOrgTByUHEoHzg3vNsApRM8zrbsxJ9mmnrGkbhUPI1SfFooJPYjsZ5B-OBNNS8532pqwG-kxPmZPunpIknRLU9ciwzU4OMKs5Zq3WwNa__QwQxQkBPAvigi898rlI6-nr2mrOK7P-D-qPAspqx0vie5rgXg9kiAnPiJFZEKEebtN9u0uvVVBI3U2cagETiBrXfGlz3Y4nsxdIh9Uzu58a6TLsD-xg2kZ7uz4bFXib4paHgJQCjOF-LQcsHusr295wcNWqgfn7Pjr4jrEARWGUHH_X5id44kTnLZi_l-mPghgJBRjXJFtcq50xFPThus81G9UKBQ02xJrISpyE_f9g382tasCrv4uzM8qNJ2QhfBmK9ZcbRGdmG6XBS24Xtnkw_ibnYFh5i9Jg5HAuthY_io7xurW5Sd0EgWy15gz7v4RTVXr5E9yQKNpYkhznL3_sMW0BTZxwW90AIVSgnsPu5Un6Bm3nHvLgCmke2rxvPEhOxkSYaw8WZf5iSoE6hD2YDNaqqsFkwdRw_u5MiR-Uwe67XcOdukQW_7IKd74yncOZc04t7B2lWBpJgJ20VbdFJFDf0NMpDcwvAEwdwlpIIvyL2yDFXS6sVq_CB3JlmiTBQpAhBTiQ4e9o9BFARn6u4SQsgKEPlLiOCIuSXmcvy5om-4ZY1occmx4UNXh0hQj9TXUwanr53UNvgh7eTPKbQ6tZD41StURNYXPKz2m5CtYwcuf_HEA1uy-H4YGNh1Gx0hUo8-7vMquBdoEI80KDxWQs_dx4aXcVsLSaYkRyWCQW00l1AiYOj0mUcacwL8mEw6p4hxqWUrU_fgQKc60WVwJGa59GBZaKkfpuovRDQzm14z_yGVG0Wx5qEI-hWDLgjU0YiAaW23kN039CL7iJsyLEob-IM3paMlNf6HXg5dpX-GTOLdGyjVR4nnJxByLo2HTVGr7z_AnJNjLsHLecRbVldrHb6GpW2MDl_5F0owsDGE5d-UHIXZ4TdjFaVQsB9EQurPCqzIblMASvk8tBnsuCu-TOwH6oxhrEy1fFwE2SCulrHQ7m-KwSbu6Yi0Q12tLlM7nc1VXpTAZh0F7SpbKAx9hOqNl7R7AM-oWVXgWsIV8fjfuRfYabGZnpSh0ftIotGY1s6rLUPZJhhQmZLYou3ATOMiXj8c1jmzi2aZWoRhEjAE3TdQag_4nDC8vPROMYVHm9bgyCZ8W5_y7QOnMjYXQX-0YhZZU6cxd8U6QX7uPPwogShiIsScH0Xh4gKZzN-cD3qn6eKh4Rn6cHXQfD7ZYC8QDdH4jhBdT2sVy0Wyqtij0iaSbscJTojBtpwaAOhnDU58-Zw8_RmVy2hgwhBEgyOnsqvSVXxYpXwuYIvRKfz-8PtfFRi9Kr2bGVcTNwW0r87cPcPvfH-bEhQ8rs6HKEWfanaR2P7_xKbvlyD4Ay7yuT7Xk8mHsjEFpZ8gr0duGM90e_JByhha23733qcqAK6P98KrzX4pSiWC8sWcsUMxU4CwEmju0TJjALUOi7ZiQX5THdup_hlZnzYCmw6lAqI40sGtZjqPqsS4blZGHFIHZTeCSCyHVYRJAjS-H-Kueb5cxr4lnDxJCVOQW-ccCCzKKo9oLuQSFwqx9-CRDG1kikB5dlHBhWrSIEmDfYpdaOGOAyU9r_w4Rc2S01QOyZwpddDww7ZEW3s_sCa26foDW_hnda-01es7ygD8v4K-Nd8EAtywdrgQNdaFb2nY1scgT_XJcZZfNNmIR8wRzyP-xBy5m_YrCsLeGQf8LbvUFtntwdbmbEhncZXzTG8MUszL-2Xwz16TvBaWvPBE8qq_T1tdjcUTO7yzMS_IQE2746bznmbnh1auW9g5a_lOLNOJzmMYRsgDEEJzh9bfnL6NpKLNUwAz-hZsKkswnazjeGK0btj53uIaDrfCdEx4KlYiNTHHdn3tvCYmLiIIAS4L-F1B_HARrLfVoef_dtce9WclotXyzEMQ3bCwk1B0XlWJd93VuAVAYNlcWY6S4MenbSvbHQGufVtwEOdiuMWC6U9SV3VFejOkvOUVNIfkW7szjFb7WXe74rjEySPriP3zudY7lXTrYQNK26XVwnZg8RFyITSHRetNdEEErFaptVrHa_fvWSF0bz2yWWOlhFXgByirOeVr94bxUod5q2KOlwoXVj9zuUs-5IxHfByUlQOxTRCJ4NnyKBXYsS19ebwiO4DkXBfHvGsVKVCnn_l5Il9JDmpMyXpVcOm14PKdVQO6xRF0ahp-o1u_KozXMwJ8Zf_XZA_xNGfAckCcMANzZ7s1VOvDYkcq9DWDmWJuTRwARae4mhVzzK2l4tDpie8gOLlF8GT3zym_ype9SVaYggXl9aQqz2pj4ZtOvThlYzx-NXkih0RErniHF10K8UKbA28GMxHVNsbVkQdKqc9Hj-8pAkjwo648KNGalwl173NRLbEQo3ectYftn2ayICdj2mYb-l_yO9BTgerTc1Uhmui9MuSWyB45N-Mo3Hq9H7f9RegmrcqA09mLElRvtaLmA4PKUHwjTrQ3FWoGYB1bPAkrHnMA-Zj_sVZRj0z0Q_2b3V3CstXfoQ4-RumzMIbAYiuMNhyM2hyIWIZ6RxM-Cq2yFFkcmWlGgGek_YNT3AbQAHmzrlanVsArhI6RUzpFFyvgyAJ0ZXkLwkIcmTngeswkIpwt31PMy7_FUzCJ_M0Mzy63TT8i2EaYTvtf8HLcUXH2qdxd80VLbuaqb7fYXT85HzEtFpGk_YARicoIXN8y4ZwsX6dIuwwjAdQtjK4VDOpUTi_tZnQCFJjidh-B-eUjJHdX1VtI9w7USWCu-77SHS9qPPqt5BeE7TSDKjkr7TPd7qEP58UYYSb-_CUUKW4KvFJhp4Vl2CW4E5ndvHJHaOJhnF9GgG2KZn5JRBbAyEj9YG8Rek900B3LrTdmQq1jU_qiDxfAXS95XQIcN0_SjlDeHtprX9fjoQ_FlygF0P9LSTBTsQiao7BPpkBlQMi_UJibFdgl5YJb4r1XgxrOPVnDZqUzxTGncjAHm5pg-fs57vVRXvYceuhGC1nYFPgIgPlACisWX2VfqllSBExUEt10imLazXqTeDTUmc1z4JQvWeEEtR5SknRUKmUEYDyJ6NO0qn_PCT8QDxQ-eNe4HcZuePg4cYavgWl_6dMZ70zjW8mXsfsAmVfCsuktpoBVbudOZJJ_amBj8GcNKntP4jW3xLjpDUV-zW6gz9Ol7sGA8JFu672B1xyeBLbOPXFISmYj0_fOueo82EQ831nhzIYEy0jpYp-p4kIzG1ES3TROxXdqoO5I_osVbmIMclTebftT2dqSFiHsUgOUIU7-jQTtIbEFjfFguj9O5SeKiqi-ORuLyzrmfZ2_25zzmoGuY4D53RNDNcJO2eFfmWCySIAKq_ip-HoMyXFW8_5evji6TZQ21i1aGuo91_rTe3Ir9WGqHa1I_FoqdLhi920f5W0VK3LY9sgsOdg8n-fLFNHTfodoPFBpu7CxASNmrZdC69oGDQIXpZ4Ae6VXure8JnFfNjhZ0kXrlY3MkMr3eftIAQ39cCygRDVeAxszoPyYx-eed4OFaAli_Rzua7B0co-wgQWxMQnXpy4eqTuRVMN1xZ8sOOBb1nyTvt2EtUG1W16KLdCT6w9_kXV9NtYV8u6AAtuqxY9gXcysuQdMqDjEUDPipA2emCJDcXl7WykzbGx4cpLFbZgv6B0yGGTyqwfX2b8RUrXLqJCWnWZNScdSpT8BcQqb8-1wQrQE3_WDqftwDxJsjqLYVCnwd9P_Cn6PloZjwKCqMUPBPvEzy6ustopdJtSdIz8vK0Es6ybn4kV64hmBnLF4NKRdU34TwTYiDFQMV3U25W64WAkOcPbhJ8elBk0cfDvC2dFbPEnyE6at5b7guHurPJRCUkb0NBUnd7O3BIWOCrGeteqZdbR6w2HnHm5T_MoGUrlRo4PZnbBaDRpHKCOK1qORDohpTS4fQfXjqXuu260jgVNGlGrrlslXiZsqdY0a4yz_En5xhRl_k1EbvI1iw7CXbpqfEDFBLkj9SuUot8TOfJBMDjGmNZFyFOWr9mwQq7LZ81bdUUADZgkeTnEYgbMvL8uldZl_a8UL-7WFmRlAO06REspPLa3V6ozNtIhxe8Nx3-CONJjc0RAlAzd0zrEH4vK2lpaDwmqQevBSpWyHS1dkstTsBSBO6KmAbRRblVm44yglY1UjuOLMSnty09BuVTwKP16cVWMj69ZLHRzmywOSLmM2HnBBflFAvEPQSfH-rV_B5CYysZoZCB_TV2IFysWnxsoOL7uWA3If-BicaNQs_08EBJKv_d1PK0kAbj2z7C9wWydQKv0gydSEyT24yRJkkuQ1rbVDjeAgqg6QAPl-xTo90mWba6ZxrqMjF_js-r-gg-iDWxxGbFFqy-TpF1G2c0uZJhz_2WHHyzxCy0_ZyBQzpQ8noIW_0hE9nnkFMmWLuHzPzss8libbp-M6BWOIyyH-lf-9XdGOGkAQSavai_nh05wWJ-PR-mxbfCl803IiK9O5BuKlNLZCPnrT30QpQNvzquh0LC3nSxeuk9ynH_-WKTwAPCp52kDmUJagLrAFFmeJduDtV3Z4twi-vNIjvYCCtk3-L5EdpnyJFeJ-v4aKLSI0PKaN_8q68__EcL_S84Zuvq3ZVAJ6sACM4mJsgzJCKWjdvYQ4oc802ABF2mgjVoW6eyflbWSzct1o0cEH0IckkSmkXmPM8VZEzAc-4a8NoVvgbr65pciNErQwxW-iW_v_3p1mFf8upNm0QOmXPb2D-JFhpxKpjXfxVm2QDTfyJxq6THKNg05t_S3qUnrydbONPd_6EymAURO9DEWNWgBbZCZUsx0PPA_QEgCY2b86G4FfItUX2iJZ2YV8gFn2C2PKjjc6af52od7YM7IXcW_0b_7fI0ortTzaI6Jm49eR_MU2FvQmxi8UtkYpYleSSJVYqmOfKm2x6wUkXfzdw3GNxj2exo58nTEEPWinhckjPgO3o7mh6LA4nb6kSqqv2VTkOF0B4fgcor52fSxehhgl0TMta_HVK8OlSe2jP8l6418OVCGGcfFlHXHp0mTK_K5qKc7z-KByOQIGZW7VID2KyRbVnoYy8cyPBCwivsYp7004rdqt5hMXuTeWMevhGYAYTK-Lyr0giK_hCw-2myRtWHnfxQ8BZ38l20NLF9PC-1pC1jhpXy-gaGyRdeeti4ViMztfrx4gTa2hCe06eRFaEycMN1xjsO0Cq7wNHg103XdISjfOqsC6eOuVkFN3N_FFys_UGO2S9lwqb04dVV0yYlw6sg0RkgOfxs7-pjYqmEo3jGjeyfbGQ5QNJYr2NJut8G0-tNhRhlNFbkoem1ROFch9z8t2OI9RcfVCC47zNUCe62Fh9R46YNwmGgKW5yohbi2FcD6pOXfsSy9qRWDojub4FBUrf6dOgWuhdQOxYvj6gLLZ750wncA9_pCHLPVOXpCB8CWXOrwJGvmz7NJDK2xmUV7rDgKtmNLMNc22xD9nWVpGaEBl0Bz6hIXZgKE0ad2TuOe_MSysK9KgUwopwChXzrl8J-bas6dFYW-9wDIwEZGYdReBzFZxnoKPBgtc3axfUznATuoJ11KdB0yg4ZEMO6ZRcRWw_83ZFTz8Z8c8syrnAU7o226jMqlIUA_RLT6OY6WNLchfAx8njgh7Xyw2mJwEhrP93JT_1qInAfEHzIK8lzDGDevw0MoriIodtC8JBfE3cYhfXNmloHk87iI7DkPF-wzGmKT_pzW0B1WNhwRZmHKqZMZKkFkrIzj5R_FDm2Ep1PKUYB3oeataT52uX4mu9y3UAlxqj6AlSrepIokdiYAzZXfzR7oAVhZWsjPo1uHCU_TF4PvXK22hxkrrhFSS0_xckiY_fc8crUd9UIFap_F8JMfBxGrhgfN5w2Vm4G2CTTVH1QJXgUwWSEFIfGUgaD4Pn3LOa9r0ihIn12ef8pYmba7simCQ6CIrV56d2UPgczRflSND4LCM36IBoPz9s4S3SLhgzwCUQSQxRMbJx7oqw78o1xSrlg-f9JB2m4oeVVPB7EQzA3IdShm5EWIy_6jQI3nDQMp3AkOBDqILZH_jmONSjh6pYXerTFFVH_nFZmcHCr6lQqO_oC9doIxrRhyfx2xdg60B7R-EewnguwVLojpRjyUaVfbERsscngNgAafFXWj2StuWg__WGNR4FXsp_FM-A-g98JaI9vJE2BIxpvJO_N9HjyR-p4MIkuqSZmeW1PPq8OqIzfN5297HwctdeIaiskQiFyx4k9mXLQXrSOijdMYk1S3jt6akorYFYruRO63zm1AGY9ORggvL_FY0AIIfTN9_3ZNI9umNIbWnLlfIPbUZnBGt1so2QdLpykEaDR3R-zgfUMr2sqJT5VALJNsMWYd-wWjAcHZerQCTJT3HtJbjxSoSJ6fWsEzqFeOk4hO-NcK9CmxpefsnKN49fyZFpY0HqAcrvsuEGpOP-3JlIj5BQdfuBgef95hywz1AfBUSP16CSn70073ApsxtoUsYIPziyZzLaPVD82Ap9oDUCy6Q8UuJ-UhMHMOBg2FsA-uYU24kkLjresT5-D7RRjuZH63e8xeU3E8zeTw8zSaB9Ztd7qypzWGhiKrMiGHs-DUtnGMuiYx7k-nYWD_S2Kz6nvjQuN9GjbAuH0Vkdfhgl8hMRFVOeEhm1wcQs96qbNCJ26gfVnpyOiXR8OF8KVTb8vaT7m11BE6ymKo="


const plaintext = decryptAES(ciphertext, key, iv, mode, padding);
console.log(plaintext);


// -----------------------------------     RSA加密（crypto）     -------------------------------------------------

 const crypto = require('crypto');

 function encryptRSA(data, publicKey) {
   const bufferData = Buffer.from(data);
   const encrypted = crypto.publicEncrypt(publicKey, bufferData);
   return encrypted.toString('base64');
 }

 function decryptRSA(data, privateKey) {
   const bufferData = Buffer.from(data, 'base64');
   const decrypted = crypto.privateDecrypt(privateKey, bufferData);
   return decrypted.toString();
 }

 const data = 'Hello World!';
 const publicKey = `-----BEGIN PUBLIC KEY-----
 -----END PUBLIC KEY-----`

 const privateKey = `-----BEGIN PRIVATE KEY-----
 -----END PRIVATE KEY-----`;


 const encrypted = encryptRSA(data, publicKey);
 console.log('Encrypted:', encrypted);

 const decrypted = decryptRSA(encrypted, privateKey);
 console.log('Decrypted:', decrypted);


  生成公钥和私钥
 const { generateKeyPairSync } = require('crypto');
 const { publicKey, privateKey } = generateKeyPairSync('rsa', {
   modulusLength: 2048,
   publicKeyEncoding: {
     type: 'spki',
     format: 'pem',
   },
   privateKeyEncoding: {
     type: 'pkcs8',
     format: 'pem',
   },
 });
 console.log(publicKey)
 console.log(privateKey)


// -----------------------------------     RSA加密（node-rsa）     -------------------------------------------------

 const CryptoJS = require('crypto-js');
 const NodeRSA = require('node-rsa');

 // RSA 加密函数
 function encryptRSA(data, publicKey) {
   // 创建 RSA 实例并导入公钥
   const rsa = new NodeRSA();
   rsa.importKey(publicKey, 'pkcs8-public-pem');

   // 使用公钥加密数据
   const ciphertext = rsa.encrypt(data, 'base64');
   return ciphertext;
 }

 // RSA 解密函数
 function decryptRSA(ciphertext, privateKey) {
   // 创建 RSA 实例并导入私钥
   const rsa = new NodeRSA();
   rsa.importKey(privateKey, 'pkcs8-private-pem');

   // 使用私钥解密数据
   const plaintext = rsa.decrypt(ciphertext, 'utf8');
   return plaintext;
 }

 const data = 'Hello, world!';

 publicKey = ''
 privateKey = ''
 encrypted = encryptRSA(data, publicKey);
 console.log('Encrypted:', encrypted);

 decrypted = decryptRSA(encrypted, privateKey);
 console.log('Decrypted:', decrypted);