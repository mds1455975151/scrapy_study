# -*- coding: utf-8 -*-

from scrapy.exceptions import DropItem
import json
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class MyPipeline(object):
    def __init__(self):
        # 打开文件
        self.file = open('data.json', 'a')
        pass

    # 该方法用于处理数据
    def process_item(self, item, spider):
        # 读取item中的数据
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    # 该方法在spider被开启时被调用。
    def open_spider(self, spider):
        pass

    # 该方法在spider被关闭时被调用。
    def close_spider(self, spider):
        pass
