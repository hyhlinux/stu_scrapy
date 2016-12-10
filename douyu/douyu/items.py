# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
    # define the fields for your item here like:
    """
    :type name:主播名
    :type imagesUrls:
    """
    name = scrapy.Field()
    imagesUrls = scrapy.Field()
    city = scrapy.Field()
    imagesPath = scrapy.Field()
