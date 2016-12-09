# coding:utf-8


class MyURL:
    HTTP = "http://"
    BAIDU = HTTP + "www.baidu.com"
	

userAgent = {
	    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36"
}

def main():
    print MyURL.BAIDU


if __name__ == '__main__':
    main()
