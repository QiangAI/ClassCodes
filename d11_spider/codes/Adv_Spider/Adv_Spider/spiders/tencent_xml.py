# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider


class TencentXmlSpider(XMLFeedSpider):
    name = 'tencent_xml'
    allowed_domains = ['ke.qq.com']
    start_urls = ['https://ke.qq.com/course/list?mt=1001&st=2002&tt=3019&price_min=1&page=1']
    iterator = 'html'  # you can change this; see the docs
    itertag = 'ul'  # change it accordingly

    def parse_node(self, response, selector):
        print('开始解析数据')
        item = {}
        print(selector)
        # item['url'] = selector.select('url').get()
        # item['name'] = selector.select('name').get()
        # item['description'] = selector.select('description').get()
        if selector.xpath('@class').get() == 'course-card-list':
            # print('\t', selector)
            # 节点过滤，
            li = selector.xpath('li')
            print(len(li))
            for co in li:
                co_ = co.xpath('h4[@class="item-tt"]/a/text()').get()
                # print('\t\t', co_)
        else:
            print('\t', '...')
        return item

    def adapt_response(self, response):
        print('得到页面')
        # 返回修正后的response
        return response

    def process_results(self, response, results):
        print('数据解析完毕', type(results), results)
        return results
