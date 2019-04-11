# -*- coding: utf-8 -*-
import scrapy


class MyspiderSpider(scrapy.Spider):
    name = 'myspider'
    allowed_domains = ['https://ke.qq.com/course/list?mt=1001&st=2002&tt=3019&price_min=1']
    start_urls = ['http://https://ke.qq.com/course/list?mt=1001&st=2002&tt=3019&price_min=1/']

    def parse(self, response):
        pass
