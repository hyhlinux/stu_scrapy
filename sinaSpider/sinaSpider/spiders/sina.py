# -*- coding: utf-8 -*-
import scrapy
import sys
import os

from sinaSpider.items import SinaspiderItem

reload(sys)
sys.setdefaultencoding("utf-8")


class SinaSpider(scrapy.Spider):
    name = "sina"
    allowed_domains = ["sina.com.cn"]
    start_urls = ["http://news.sina.com.cn/guide/"]

    def parse(self, response):
    	print response.body
        pass
