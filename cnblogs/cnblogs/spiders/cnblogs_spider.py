# -*- coding: utf-8 -*-
import scrapy
from cnblogs.items import CnblogsItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spider import Rule
from scrapy.http import Request


class CnblogsSpiderSpider(scrapy.Spider):
    name = 'cnblogs_spider'
    allowed_domains = ['cnblogs.com']
    start_urls = []
    for i in range(1, 35):
        print i
        url = "http://www.cnblogs.com/kevingrace/p/?page=%s" % i
        print url
        start_urls.append(url)
    print start_urls

    def parse(self, response):
        item = CnblogsItem()
        # print response.xpath('.//*[@id="myposts"]/div[@class="PostList"]')
        # url = scrapy.Selector('//*[@id="myposts"]/div[11]/div/a[9]/@href').extract()
        # print url
        # url = "http://www.cnblogs.com" + url
        # print url

        for title_list in response.xpath('.//*[@id="myposts"]/div[@class="PostList"]'):
            item['title_name'] = title_list.xpath('./div[@class="postTitl2"]/a/text()').extract()
            item['title_url'] = title_list.xpath('./div[@class="postTitl2"]/a/@href').extract()
            yield item
