# -*- coding: utf-8 -*-
import scrapy


class DemoApiSpider(scrapy.Spider):
    name = 'demo_api'
    allowed_domains = ['ke.qq.com']
    start_urls = ['http://ke.qq.com/']

    def parse(self, response):
        pass
