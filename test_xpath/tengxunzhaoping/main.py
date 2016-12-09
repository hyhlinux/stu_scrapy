# coding:utf-8


import urllib
import urllib2
import json

from bs4 import BeautifulSoup


class Spider(object):
    """
    docstring for tiebaSpider
    url:http://tieba.baidu.com/
    tiebai搜索:http://tieba.baidu.com/f?kw=
    teibai:
    """

    def __init__(self):
        self.url = "http://hr.tencent.com/position.php?&start=10#a"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36"
                        }
        request = urllib2.Request(self.url, headers=self.headers)
        response = urllib2.urlopen(request)
        resHtml = response.read()

        html = BeautifulSoup(resHtml, 'lxml')

        # css
        select = html.select('tr[class="even"]')
        select2 = html.select('tr[class="odd"]')

        select += select2
        positionList = []
        for each in select:
            name = each.select('td a')[0].get_text()
            link = 'http://hr.tencent.com/' + \
                each.select('td a')[0].attrs['href']
            leibie = each.select('td')[1].get_text()
            number = each.select('td')[2].get_text()
            city = each.select('td')[3].get_text()
            time = each.select('td')[4].get_text()

            item = dict(name=name, link=link, leibie=leibie,
                        number=number, city=city, time=time)

            positionList.append(item)

        # print positionList

        # output = open('tengcent.json', 'w')
        with open('tengcent.json', 'w') as output:
            line = json.dumps(positionList, ensure_ascii=False)
            output.write(line.encode('utf-8'))


def main():
    spider = Spider()
    pass
if __name__ == '__main__':
    main()
