#!/usr/bin/env python
# encoding: utf-8

import scrapy
import sys
reload(sys)
# Python默认环境编码是ascii
sys.setdefaultencoding("utf-8")


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = []

    def start_requests(self):
        file_object = open('movie_name.txt', 'r')
        try:
            url_head = "https://movie.douban.com/subject_search?search_text="
            for line in file_object:
                self.start_urls.append(url_head + line)

            for url in self.start_urls:
                yield  self.make_requests_from_url(url)
        finally:
            file_object.close()

    def parse(self, response):
        pass