# coding:utf-8
import urllib2

URL_BAIDU = 'http://www.baidu.com'


def test_url(url=URL_BAIDU):
    response = urllib2.urlopen(url)
    print response
    if response:
        html = response.read()
        return html


def test_req(url=URL_BAIDU):
    request = urllib2.Request(url=url)
    response = urllib2.urlopen(request)
    html = response.read()
    return html


def main():
    # print test_url(url)
    print test_req()
if __name__ == '__main__':
    main()
