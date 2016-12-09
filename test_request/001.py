# coding:utf-8

import requests

r = requests.get('http://python.org')
print r.status_code
print r.content


payload = dict(key1='value1', key2='value2')
r = requests.post("http://httpbin.org/post", data=payload)
# print r
# print(r.text)


data = dict(wd="长城")
headers = {
    "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"
}

url = 'http://www.baidu.com/s?'
# req = requests.get(url, params=data, headers=headers)
# print req.text.encode('utf-8')


url = 'https://www.lagou.com/jobs/positionAjax.json?'
data = dict(kw='python')
req = requests.post(url, data=data, headers=headers)
# print req.text.encode('utf-8')
print '---------'

with open('lagou.json', 'w') as f:
    f.write(req.text.encode('utf-8'))
