# coding:utf-8

import urllib2
import urllib
import config

url = 'https://www.lagou.com/jobs/list_'
city
yx


def tiebaSpider(kw='qinshimingyue', beginPage=1, endPage=3):
    name = kw
    kw = urllib.urlencode(dict(kw=kw))
    beginPage = int(beginPage)
    endPage = int(endPage)
    print kw, beginPage, endPage
    for page in xrange(beginPage, endPage + 1):
        page = (page - 1) * 50
        url = "http://tieba.baidu.com/f?{}&pn={}".format(str(kw), str(page))
        data = loadPage(url)
        # print data
        htmlSave(data, 'kw_{}_{}{}'.format(name, str(page), '.html'))


def htmlSave(html, filename):
    with open(filename, 'w') as f:
        f.write(html)


def loadPage(url):
    print 'load:', url
    request = urllib2.Request(url, headers=config.userAgent)
    response = urllib2.urlopen(request)
    if response.code == 200:
        return response.read()
    else:
        return "无法获取请求数据, 错误码:{}".format(response.code)


def main():
    # tiebaSpider()
    while True:
        kw = raw_input("请输入要爬取的贴吧:")
        beginPage = raw_input("开始页:")
        endPage = raw_input("结束页:")
        if all((kw, beginPage, endPage)):
            tiebaSpider(kw, beginPage, endPage)
            break
        else:
            tiebaSpider()


if __name__ == '__main__':
    main()
