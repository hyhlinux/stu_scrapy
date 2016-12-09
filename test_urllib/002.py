#coding:utf-8
# coding:utf-8
import config
import urllib2

url = 'http://www.baidu.com'

userAgent = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36"
}

request = urllib2.Request(url, headers = userAgent)
request.add_header("Connection", "keep-alive")

print request.get_header(header_name="Connection")


# response = urllib2.urlopen(req)
# print response
# html = response.read()
# print 'html:', html





