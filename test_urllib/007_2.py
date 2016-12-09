# coding:utf-8
import urllib2
import cookielib


filename = 'cookie.txt'

cookie = cookielib.LWPCookieJar(filename)

handler = urllib2.HTTPCookieProcessor(cookie)

opener = urllib2.build_opener(handler)

response = opener.open("http://www.baidu.com")

cookie.save()
