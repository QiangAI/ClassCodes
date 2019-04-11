# coding = utf-8
import scrapy


class HomeSpider(scrapy.Spider):
    name = 'home'
    start_urls = [
        'https://ke.qq.com/course/list?mt=1001&st=2002&tt=3019&price_min=1',
    ]

    def parse(self, response):
        self.log('XXXXX:response')
        self.log('XXXXX:{}'.format(response))
