#!/usr/bin/env python
# -*- coding:utf-8 -*-

# import urllib
# import urllib2
import requests
from lxml import etree
import django



class tiebaSpider():
    def __init__(self):
        # self.beginPage = int(raw_input("请输入起始页："))
        # self.endPage = int(raw_input("请输入终止页："))
        print ('__init__')
        self.beginPage = 0
        self.endPage = 0
        self.s = 49943
        self.url = 'http://www.qiushibaike.com/8hr/page'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"}
        self.num = 1

    def spiderWork(self):
        if not all((self.beginPage, self.endPage)):
            self.beginPage = 2
            self.endPage = 2

        print('---')
        for page in range(self.beginPage, self.endPage + 1):
            myUrl = '{}/{}?s={}'.format(self.url, page, self.s)
            content = self.loadPage(myUrl)
            self.writeContent(content)

    def loadPage(self, url):
        # 按照参数构造一个http请求信息，返回一个构造好的请求对象
        req = requests.get(url, headers=self.headers)

        # 按照构造内容发送这个请求，返回一个 类文件 对象
        html = req.text.encode('utf-8')
        print html

        selector = etree.HTML(html)
        # # print type(selector)

        # # 抓取当前页面的所有content
        content = selector.xpath('*//div[@class="content"]/span')

        # # content[0].text  是段子内容
        return content

    def writeContent(self, content):
        print "正在存储文件 ...", self.num
        with open('qiushibaike.txt', 'w') as f:
            for line in content:
                f.write(line.text.encode('utf-8'))
                flag = u'\n-----------\n'.encode('utf-8')
                f.write(flag)
                self.num += 1

if __name__ == '__main__':
    spider = tiebaSpider()
    print spider
    spider.spiderWork()

#=================================================================
