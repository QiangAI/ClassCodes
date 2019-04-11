# -*- coding: utf-8 -*-
import scrapy


class TcSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['ke.qq.com']
    start_urls = ['https://ke.qq.com/']

    def parse1(self, response):
        print('处理爬取结果')
        print(type(response))

        # return  ['数据', '下一次爬取的url']
