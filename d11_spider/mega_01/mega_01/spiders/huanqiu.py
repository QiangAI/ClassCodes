# -*- coding: utf-8 -*-
import scrapy


class HuanqiuSpider(scrapy.Spider):
    name = 'huanqiu'  # 爬虫名
    allowed_domains = ['http://www.huanqiu.com']
    start_urls = ['http://www.huanqiu.com/', 'https://www.baidu.com']

    def parse(self, response):
        print('hello 我是爬虫我怕谁！')
        print(type(response))
