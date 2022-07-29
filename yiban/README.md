## 易班登录逆向
### 是RAS加密，找到相关加密代码扣下来，补全环境

****

**注意：** 在调试环境报错：ASN1.prototype.getHexStringValue = function() {
  ReferenceError: ASN1 is not defined
  
  ASN1是一个JS解码器，可以解码任何有效的Base64编码或十六进制编码的DER或BER结构，一般浏览器已内置的有，大部分js调试器是没有的
  
  解决方法：
  ```
    // 定义
    var window = global;
```