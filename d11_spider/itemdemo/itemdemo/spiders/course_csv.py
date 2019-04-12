# -*- coding: utf-8 -*-
from scrapy.spiders import CSVFeedSpider


class CourseCsvSpider(CSVFeedSpider):
    name = 'course_csv'
    allowed_domains = ['127.0.0.1']
    start_urls = ['http://127.0.0.1/course.csv']
    headers = ['course_link',
               'course_name',
               'course_number',
               'course_organization',
               'course_price',
               'course_status']
    delimiter = ','

    def parse_row(self, response, row):
        i = {}
        print(row['course_name'], '\t', row['course_price'])
        # i['url'] = row['url']
        # i['name'] = row['name']
        # i['description'] = row['description']
        return i
