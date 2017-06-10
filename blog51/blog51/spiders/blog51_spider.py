# coding=utf-8

import scrapy
import re
# 引入容器
from blog51.items import Blog51Item


class Blog51Spider(scrapy.Spider):
    # 设置name
    name = "Blog51Spider"
    # 设定域名
    allowed_domains = ["51cto.com"]
    # 填写爬取地址
    start_urls = ["http://oldboy.blog.51cto.com/all/2561410"]
    start_urls = ["http://liqingbiao.blog.51cto.com/all/3044896"]
    start_urls = ["http://liqingbiao.blog.51cto.com/all/3044896/page/2"]
    start_urls = ["http://liqingbiao.blog.51cto.com/all/3044896/page/3"]

    # 编写爬取方法
    def parse(self, response):
        # 实例一个容器保存爬取的信息
        item = Blog51Item()

        # 这部分是爬取部分，使用xpath的方式选择信息，具体方法根据网页结构而定
        # 先获取文章列表的整个信息块
        # print response.xpath('.//div[@class="artList box"]')
        for title in response.xpath('.//div[@class="artList box"]//li'):
            # 获取文章的类型
            item['title_type'] = title.xpath('.//span/text()').extract()[0].strip().strip("[]")
            # 获取文章名称
            item['title_name'] = title.xpath('.//a/text()').extract()[0].strip()
            # 获取文章发表时间
            item['title_time'] = title.xpath('.//em/text()').extract()[0].strip()
            # 获取点击量
            cc = title.xpath('.//span[@class="artList_hits"]/text()').extract()[0].strip()
            item['title_hits'] = re.findall(r"\d+\.?\d*", cc)[0]
            # 获取评论量
            cc = title.xpath('.//span[@class="artList_replies"]/text()').extract()[0].strip()
            item['title_replies'] = re.findall(r"\d+\.?\d*", cc)[0]
            # 返回信息
            yield item
