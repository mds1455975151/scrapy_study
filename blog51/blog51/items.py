# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Blog51Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class Blog51Item(scrapy.Item):
    """
        用户获取51cto某用户的博客文章列表
    """
    # 文章类型
    title_type = scrapy.Field()
    # 文章名称
    title_name = scrapy.Field()
    # 文章发表日期
    title_time = scrapy.Field()
    # hits点击量
    title_hits = scrapy.Field()
    # replies评论量
    title_replies = scrapy.Field()
