# coding:utf-8
import config
import urllib2

url = 'http://www.baidu.com'

userAgent = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36"
}

req = urllib2.Request(url, headers=userAgent)
print req
response = urllib2.urlopen(req)
print response
html = response.read()
print 'html:', html





