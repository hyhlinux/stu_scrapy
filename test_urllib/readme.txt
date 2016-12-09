001:urllib.open()
002:request
0003:urllib 库中urlencode 进行编码.
	练习1.renren
		2.douban.com
		3.qq.com

005: 
	代理 	---> 代理池
	openner 

006:debug 查看收发包情况.


007:cookie 

	CookieJar 基类
	Cookielib


	FileCookieJar
	MozillaCookie

	cookie三种读取方式.
	cookie: 内部实现了__iter__ , cookie是{}, 排序保存.
			使用了yield

009:百度贴吧爬取.
第一页:http://tieba.baidu.com/f?kw=qinshimingyue
第二页:http://tieba.baidu.com/f?kw=%E7%A7%A6%E6%97%B6%E6%98%8E%E6%9C%88&pn=50
pn = (page-1)*50

