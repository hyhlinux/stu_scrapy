# coding:utf-8
import urllib2
import cookielib


filename = 'cookie.txt'
cookie = cookielib.LWPCookieJar()
cookie.load(filename)

# 从文件中读取cookie内容到变量，忽略cookie的使用时效
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)

# 创建请求的request
req = urllib2.Request("http://www.baidu.com")

# 利用urllib2的build_opener方法创建一个opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

response = opener.open(req)

print response.read()
