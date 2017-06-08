#!/usr/bin/env python
# encoding: utf-8

import sys
reload(sys)
# Python默认环境编码是ascii
sys.setdefaultencoding("utf-8")
import scrapy


class DoubanSpider(scrapy):
    name = "douban"
    allowed_do