# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys
from scrapy import signals
reload(sys)
sys.setdefaultencoding("utf-8")

class SinaspiderPipeline(object):
    def process_item(self, item, spider):
        sonUrls = item['sonUrls']

        # 文件名为子链接url中间部分，并将 / 替换为 _，保存为 .txt格式
        filename = sonUrls[7:-6].replace('/','_')
        filename += ".txt"

        with open(item['subFilename']+'/'+filename, 'w') as fp:
            fp.write(item['content'])

        return item
