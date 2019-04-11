# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TtCourseSpider(CrawlSpider):
    name = 'tt_course'
    allowed_domains = ['ke.qq.com']
    start_urls = ['https://ke.qq.com/course/list/Python']

    rules = (
        Rule(
            LinkExtractor(allow=r'course/\d{6}'),
            callback='parse_item',
            # cb_kwargs={'name':'louis'},
            follow=False,
            process_links='p_link',
            process_request='p_request'
        ),
    )

    def parse_item(self, response):
        name = response.xpath('//*[@id="js-imgtext"]/div[2]/h1/span/text()').get()
        # item = {}
        # item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # item['name'] = response.xpath('//div[@id="name"]').get()
        # item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
        print(name)
        # return ['数据'，‘‘请求’’]

    def p_link(self, param):
        print('p_link', type(param), param)
        # 实现链接的过滤
        # return param
        return

    def p_request(self, param):
        # 请求之前的处理
        print('p_request', type(param))
        return param
