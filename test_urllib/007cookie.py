# coding:utf-8

import urllib2
import cookielib


cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)

openner = urllib2.build_opener(handler)


url = 'http://www.baidu.com'
response = openner.open(url)
print len(cookie), type(cookie)

cookies = ""
for item in cookie:
    cookies = cookies + item.name + "=" + item.value + ";"

print cookies[::-1]
