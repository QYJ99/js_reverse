# -*- coding: utf-8 -*-
# @Time    : 2021/12/16 15:42
# @Author  : Cat
# @FileName: scmor.py


# https://ac.scmor.com/

import execjs

with open("./enc.js","r", encoding="utf-8") as f:  # spiders/module/
    js_code = f.read()
ctx = execjs.compile(js_code,) # cwd=r"C:\Users\thouger\AppData\Roaming\npm\node_modules"
urls = ["ZAM0RgYmLl0Ne3pZfjZxATgbMlcpJD8HKEMyGDdlfBVsMDcBbzgAf2xjJEhoDDBWYBkAFyE1eAghLA8M","U3kwBQctIQAjMHZdVC1xRDs5LVQqURUfKxwQGjQACBZ5VysGVytwfmVgDQBVKSMZYRpbGwxAFhYOKl5JAWZRDw4EXzwWBwMT","U3kwBQctIQAjMHZPbldbRQApNUc/DiMZEH1WBQ9bCV8=","U3kwBQctIQAjMHZPbhwFRjg2VkUqNyAWP31WBQ8AARQ=","U3kwBQctIQAjMHYGU1ZTRAMmD0cQDisWF31WBzRLBAhXDV1R","U3kwBQctIQAjMHZdVC1xRDs5LVQqURUfKxwQGjQACBZ5VysGVytwfmVgDQBVKSBVYgpaFwsqZBAjOXtEOwdQEyFxVzEaBHpY","U3kwBQctIQAjMHZdVC1xRDs5LVQqURUfKxwQGjQACBZ5VysGVytwfmVgDQBVKSBVYgpaFwsqZBAjOXtEOwdQEyFzKnsaQgpY","U3kwBQctIQAjMHYBUzJmSwApNlsQUVQZKBwbAyFcYxRWJ11R","U3kwBQctIQAjMHZPbldYRwMmJVc/DhUHEEM5Bw9cfw1RN1AGVAZxcg=="]
for url in urls:
    res = ctx.call("strdecode",url)
    print(res)

