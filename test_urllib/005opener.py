# coding:utf-8

import urllib2


proxyWork = False


openProxy = urllib2.ProxyHandler({"http": "123.207.174.233:80"})
nullProxy = urllib2.ProxyHandler({})

if proxyWork:
    openner = urllib2.build_opener(openProxy)
else:
    openner = urllib2.build_opener(nullProxy)
# urllib2.install_opener()  #全局的opner
url = "http://www.baidu.com"
response = openner.open(url)
print response.read()
