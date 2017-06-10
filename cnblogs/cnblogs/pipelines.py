# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import sys
import webbrowser
reload(sys)
sys.setdefaultencoding("utf-8")


class CnblogsPipeline(object):
    def __init__(self):
        # 打开文件
        self.file = open('data.json', 'a')

    # 该方法用于处理数据
    def process_item(self, item, spider):
        # 读取item中的数据
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item





