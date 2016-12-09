# coding:utf-8
import requests

# req = requests.get("https://www.baidu.com/", verify=True)
# print req.text.encode('utf-8')

# req = requests.get("https://kyfw.12306.cn/otn/", verify=True)
# print req.text.encode('utf-8')

req = requests.get("https://tplinux.cn/", verify=True)
print req.text.encode('utf-8')
print req.status_code
