#!/usr/bin/env python
# coding:utf-8


import urllib2
import re


class Spider:

    def __init__(self):
        self.str = '--------我的分割线------------'.decode('utf-8').encode('gbk')
        self.run = True
        self.filename = 'duanzi.txt'
        self.page = 1

    def loadPage(self):
        url = "http://www.neihan8.com/article/list_5_" + \
            str(self.page) + '.html'
        userAgent = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36"
        }

        request = urllib2.Request(url, headers=userAgent)
        response = urllib2.urlopen(request)
        html = response.read()

        # print html
        # return html
        pattern = re.compile(r'<div\sclass="f18 mb20">(.*?)</div>', re.S)
        htmlList = pattern.findall(html)

        for each in htmlList:
            self.dealPage(each)

    def dealPage(self, data):
        each = data.replace("<p>", "").replace(
            "<br>", "").replace("<br />", "").replace("</p>", "")
        self.writePage(each)

    def writePage(self, each):
        with open(self.filename, 'a') as f:
            f.write(each)
            f.write(self.str)

    def work(self):
        while self.run:
            enter = raw_input("按下回车继续:")
            if enter == "quit":
                self.run = False
            htmlList = self.loadPage()
            self.dealPage(htmlList)
            self.page += 1


if __name__ == '__main__':
    spider = Spider()
    # spider.loadPage()
    spider.work()
