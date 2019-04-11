# -*- coding: utf-8 -*-
import scrapy


class FeeCourse(scrapy.Item):
    org = scrapy.Field()
    price = scrapy.Field()


class TtCourseSpider(scrapy.Spider):
    name = 'tt_course'
    allowed_domains = ['ke.qq.com']
    url = 'https://ke.qq.com/course/list/python爬虫工程师?price_min=1&page=%d'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Safari/605.1.15'
    }
    page_no = 1

    def start_requests(self):
        # 构建爬取的网页
        request = scrapy.Request(
            url=self.url % self.page_no,
            callback=self.extract_course,
            method='GET',
            headers=self.headers, errback=self.error_handle)
        return [request]

    def error_handle(self, err):
        print('无数据可爬')

    def extract_course(self, response):
        output = []
        print('开始处理数据')
        # xpath
        courses = response.xpath('//div[@data-report-module="middle-course"]/ul/li')
        for course in courses:
            item_ = FeeCourse()
            # 机构
            item_['org'] = course.xpath('div/span/a/@title').get()
            # 价格
            item_['price'] = course.xpath('div/span[@class="line-cell item-price"]/text()').get()
            output.append(item_)
        print('-------------------')
        if self.page_no <= 10:
            self.page_no += 1
            request = scrapy.Request(
                url=self.url % self.page_no,
                callback=self.extract_course,
                method='GET',
                headers=self.headers, dont_filter=True, errback=self.error_handle)
            output.append(request)

        return output
