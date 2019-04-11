# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TencentCrawlSpider(CrawlSpider):
    name = 'tencent_crawl'
    allowed_domains = ['ke.qq.com']
    start_urls = ['https://ke.qq.com/course/list?mt=1001&st=2002&tt=3019&price_min=1&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'course/\d{6}'),
             callback='parse_item', cb_kwargs={'name': 'Louis'},
             follow=True,
             process_links='proc_links',
             process_request='proc_request'),
    )

    def parse_item(self, response, **kwargs):
        print(kwargs)
        print(response.url)
        # splits = response.url.split('/')
        # print(splits[-1])
        # if int(splits[-1]) == 284170:
        #     print('输出', response.text)
        item = {}
        # 在这儿解析数据
        return item
        # return [item]

    def proc_links(self, param):
        print('links:', type(param))
        return param  # 不返回就没有链接

    def proc_request(self, param):
        print('request:', type(param))
        return param  # 不返回就没有请求就没有
