# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider


class CourseXmlSpider(XMLFeedSpider):
    name = 'course_xml'
    allowed_domains = ['ke.qq.com']
    start_urls = ['https://ke.qq.com/course/list/Python开发?page=2']
    iterator = 'html'  # iternodes . html . xml
    itertag = 'div'  # change it accordingly

    def parse_node(self, response, selector):
        item = {}
        # print('数据解析', selector)
        # 开始解析
        node = selector.xpath('@data-report-module').get()
        if node == 'middle-course':
            # 处理数据
            course_nodes = selector.xpath('ul/li')
            for course in course_nodes:
                # 训话获取每个数据
                course_name = course.css('h4 > a::text')
                # course_name = course.xpath('h4/a/text()').get()
                print(course_name)

        return item

    # def adapt_response(self, response):
    #     # print('数据解析前的处理....')
    #     # 可以对response进行那个额外处理
    #     return response
    #
    # def process_results(self, response, results):
    #     # print('解析后的善后工作！')
    #     return results
