# coding:Utf-8
import requests
import threading
import json
from Queue import Queue
from lxml import etree

class ThreadCrawl(threading.Thread):
    """
    用来抓取网页的线程

    """

    def __init__(self, threadName, pageQueue):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.pageQueue = pageQueue
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36"
        }

    def run(self):
        self.pageSpider()

    def pageSpider(self):
        while True:
            if self.pageQueue.empty():
                break
            else:
                page = self.pageQueue.get()
                print('{}...page:{}...'.format(self.threadName, page))
                url = "http://www.qiushibaike.com/8hr/page/" + str(page)
                html = requests.get(url, headers=self.headers)
                dataQueue.put(html.text.encode('utf-8'))
                print('新建data{}...page:{}...dataqueue{}'.format(self.threadName, page, dataQueue.qsize()))

#--------------------------------


class ThreadParse(threading.Thread):
    """
    用来解析抓取网页的线程

    """

    def __init__(self, threadName, dataQueue):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.dataQueue = dataQueue
        self.filename = fd
        self.lock = lock
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36"
        }

    def run(self):
        self.dataSpider()

    def dataSpider(self):
        while True:
            if self.dataQueue.empty():
                break
            else:
                pageHtmlData = self.dataQueue.get()
                print('{}..parse{}'.format(self.threadName, len(pageHtmlData)))
                self.parseData(pageHtmlData)

    def parseData(self, html):
        """
        解析html数据
        """
        global thradNum
        html = etree.HTML(html)
        result = html.xpath('//div[contains(@id, "qiushi")]')

        duanziList = []
        for each in result:
            items = {}
            # 图片链接
            items['imgUrl'] = each.xpath(
                '//div[@class="author clearfix"]//img/@src')[0]
            # 用户昵称
            items['nickName'] = each.xpath('.//h2')[0].text
            # 段子内容
            items['content'] = each.xpath(
                './/div[@class="content"]/span')[0].text
            # 点赞
            items['zan'] = each.xpath('.//i')[0].text
            # 评论数
            items['comment'] = each.xpath('.//i')[1].text

            #锁也会自动打开和关闭.
            #__enter__ __exit__ 
            '''
                with open(self.filename, 'r') as file:
                    data 
            '''
            with self.lcok:
                self.file.write(json.dumps(items, ensure_ascii=False))



# html队列.
dataQueue = Queue()
# 创建互斥锁
lock = threading.Lock()
threadName = 0

fd = None
def main():
    global fd
    fd = open('duanzi.json','a')
    # 分页队列
    pageQueue = Queue(3)
    for page in xrange(2, 5):
        pageQueue.put(page)

    # 爬取线程集合
    crawlThread = []
    crawlList = ['craw_1', 'craw_2', 'craw_3']

    for theadNmae in crawlList:
        thread = ThreadCrawl(theadNmae, pageQueue)
        thread.start()
        crawlThread.append(thread)

    # 解析线程集合
    parseThread = []
    parseList = ['parse_1', 'parse_2', 'parse_3']

    for theadNmae in parseList:
        thread = ThreadParse(threadName, dataQueue)
        thread.start()
        parseThread.append(thread)



if __name__ == '__main__':
    main()
