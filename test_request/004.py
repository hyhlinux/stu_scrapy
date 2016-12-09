# coding:utf-8

import requests
import json


# url = 'http://www.baidu.com'
# req = requests.get(url)
# print req.cookies


url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')
req = requests.get(url, cookies=cookies)
print req.text
# {
#   "cookies": {
#     "cookies_are": "working"
#   }
# }
#
#发送cookie
cookies = dict(BSD='working')
req = requests.get(url, cookies=cookies)
print req.text
# {
#   "cookies": {
#     "BSD": "working"
#   }
# }
