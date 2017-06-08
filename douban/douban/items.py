# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy



class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class TutorialItem(scrapy.Item):
    # 电影名称
    movie_name = scrapy.Field()
    # 电影导演
    movie_director = scrapy.Field()
    # 电影编剧
    movie_writer = scrapy.Field()
    # 电影演员
    movie_roles = scrapy.Field()
    # 电影语言
    movie_language = scrapy.Field()
    # 上映时间
    movie_date = scrapy.Field()
    # 时常xx分钟
    movie_long = scrapy.Field()
    # 电影描述
    movie_description = scrapy.Field()
