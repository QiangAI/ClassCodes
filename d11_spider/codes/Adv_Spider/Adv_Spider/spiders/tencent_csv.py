# -*- coding: utf-8 -*-
from scrapy.spiders import CSVFeedSpider


class TencentCsvSpider(CSVFeedSpider):
    name = 'tencent_csv'
    allowed_domains = ['127.0.0.1']
    start_urls = ['http://127.0.0.1/course.csv']
    delimiter = ','
    quotechar = ''
    headers = ['course_link', 'course_name', 'course_number', 'course_organization', 'course_price', 'course_status']

    # headers = ['id', 'name', 'description', 'image_link']
    # delimiter = '\t'

    # Do any adaptations you need here
    # def adapt_response(self, response):
    #    return response

    def parse_row(self, response, row):
        i = {}
        # print(self.delimiter, self.headers, self.quotechar)
        # print(row)
        print('解析中......')
        i['数据'] = '假设数据'
        i['整数'] = 20
        return i

    def adapt_response(self, response):
        print('解析前')
        return response

    def process_results(self, response, results):
        print('解析后')
        print(results)
        return results
