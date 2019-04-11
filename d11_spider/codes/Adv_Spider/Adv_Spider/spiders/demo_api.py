# -*- coding: utf-8 -*-
import logging

import scrapy


class DemoItem(scrapy.Item):
    user_name = scrapy.Field()
    user_age = scrapy.Field()
    user_hobby = scrapy.Field()


class DemoApiSpider(scrapy.Spider):
    name = 'demo_api'
    allowed_domains = ['ke.qq.com']

    # start_urls = ['https://ke.qq.com/course/list?mt=1001&st=2002&tt=3019&price_min=1&page=1']

    def __init__(self, username_, *args, **kwargs):
        super(DemoApiSpider, self).__init__(*args, **kwargs)
        print('构造器：username', username_)
        self.username = username_

    def start_requests(self):
        request1 = scrapy.Request(url='https://ke.qq.com/course/list?mt=1001&st=2002&tt=3019&price_min=1&page=1',
                                  callback=self.parse_request1,
                                  method='GET',
                                  headers=None,
                                  body=None,
                                  cookies=None,
                                  dont_filter=False)
        request2 = scrapy.Request(url='https://ke.qq.com/course/list?mt=1001&st=2002&tt=3019&price_min=1&page=1',
                                  callback=self.parse_request2,
                                  method='GET',
                                  headers=None,
                                  body=None,
                                  cookies=None,
                                  dont_filter=True)
        request3 = scrapy.Request(url='https://ke.qq.com/course/list?mt=1001&st=2002&tt=3019&price_min=1&page=1',
                                  callback=self.parse_request9,
                                  method='GET',
                                  headers=None,
                                  body=None,
                                  cookies=None,
                                  dont_filter=True)
        # return [request1, request2]
        # return request1, request2
        return [request3]

    def parse_request9(self, response):
        # 下面代码在运行时必须使用-a参数项运行，否则报错。
        # scrapy crawl demo_api --nolog  -a username=靓仔
        print('参数属性：username', self.username)

    def parse_request8(self, response):
        print('爬取百度翻译')
        return [
            {
                '用户': '黄金花',
                '年龄': 18,
                '爱好': '涂脂，抹粉'
            }
        ]

    def parse_request7(self, response):
        print('爬取腾讯课堂')
        request_ = scrapy.Request(url='https://fanyi.baidu.com',
                                  callback=self.parse_request8,
                                  method='GET',
                                  headers=None,
                                  body=None,
                                  cookies=None,
                                  dont_filter=True)
        return [request_,
                {
                    '用户': '赵德柱',
                    '年龄': 20,
                    '爱好': '喝啤，撸串'
                }]

    def parse_request6(self, response):
        print('爬取百度翻译')

    def parse_request5(self, response):
        print('爬取腾讯课堂')
        print(response.url)
        print(response.urljoin('my.html'))
        print(response.urljoin('https://fanyi.baidu.com'))
        request_ = scrapy.Request(url='https://fanyi.baidu.com',
                                  callback=self.parse_request6,
                                  method='GET',
                                  headers=None,
                                  body=None,
                                  cookies=None,
                                  dont_filter=True)
        return [request_]

    def parse_request4(self, response):
        item1 = DemoItem()
        item1['user_name'] = '赵德柱'
        item1['user_age'] = 18
        item1['user_hobby'] = '喝啤酒，撸串'
        item2 = DemoItem()
        item2['user_name'] = '黄金花'
        item2['user_age'] = 20
        item2['user_hobby'] = '涂脂，抹粉'
        return [item1, item2]

    def parse_request3(self, response):
        # 解析response获得需要的数据，这里不解析response，直接产生模拟的数据
        return [
            {
                '用户': '赵德柱',
                '年龄': 18,
                '爱好': '喝啤酒，撸串'
            },
            {
                '用户': '黄金花',
                '年龄': 20,
                '爱好': '涂脂，抹粉'
            },
        ]

    def parse_request1(self, response):
        print('解析第01个请求请求')

    def parse_request2(self, response):
        print('解析第02个请求请求')

    def close(spider, reason):
        print('爬虫关闭')

    def parse(self, response):
        # print(self.name, '\n\t|-', type(self.name))
        # print(self.allowed_domains, '\n\t|-', type(self.allowed_domains))
        # print(self.start_urls, '\n\t|-', type(self.start_urls))
        # print(self.custom_settings, '\n\t|-', type(self.custom_settings))     # 没有设置，默认返回None
        # print(self.crawler, '\n\t|-', type(self.crawler))
        # print(self.settings, '\n\t|-', type(self.settings))
        # print(self.logger, '\n\t|-', type(self.logger))
        # print(self.logger.name)
        #
        self.log('消息:%d' % 20, level=logging.INFO)
        self.logger.log(logging.INFO, '消息:%d', 20)

        self.log('消息:%d' % 20, level=logging.INFO, exc_info=True)  # 打印执行信息与栈信息
        self.logger.log(logging.INFO, '消息:%d', 20, stack_info=True)  # 打印执行信息与栈信息

        self.logger.log(logging.INFO, '消息:%d', 20, exc_info=True, stack_info=True)
