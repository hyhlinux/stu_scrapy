# coding:utf-8

import urllib2
# 打印收发包信息.
httpHeadler = urllib2.HTTPHandler(debuglevel=1)
openner = urllib2.build_opener(httpHeadler)
# urllib2.install_opener()  #全局的opner
url = "http://www.baidu.com"
response = openner.open(url)
print response.read()

"""
send: 'GET / HTTP/1.1\r\nAccept-Encoding: identity\r\nHost: www.baidu.com\r\nConnection: close\r\nUser-Agent: Python-urllib/2.7\r\n\r\n'
reply: 'HTTP/1.1 200 OK\r\n'
header: Date: Mon, 05 Dec 2016 08:07:15 GMT
header: Content-Type: text/html; charset=utf-8
header: Transfer-Encoding: chunked
header: Connection: Close
header: Vary: Accept-Encoding
header: Set-Cookie: BAIDUID=067C895B8C96479A78673E6D23BEB3A6:FG=1; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
header: Set-Cookie: BIDUPSID=067C895B8C96479A78673E6D23BEB3A6; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
header: Set-Cookie: PSTM=1480925235; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
header: Set-Cookie: BDSVRTM=0; path=/
header: Set-Cookie: BD_HOME=0; path=/
header: Set-Cookie:
"""
