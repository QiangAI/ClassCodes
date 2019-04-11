# -*- coding: utf-8 -*-
import scrapy
from Scra_DataFlow.items import ScraDataflowItem


class CourseSpider(scrapy.Spider):
    name = 'course'
    allowed_domains = ['ke.qq.com']
    start_urls = ['https://ke.qq.com/course/list?mt=1001&st=2002&tt=3019&price_min=1&page=1']

    def parse(self, response):
        # 2019-02-14 15:00:14 [course] DEBUG: <class 'scrapy.http.response.html.HtmlResponse'>
        # self.log(type(response))
        # utf-8
        # self.log(response.encoding)
        # <Selector xpath=None data='<html lang="zh">\n<head>\n    <meta charse'>
        # self.log(response.selector)
        # self.log(response.text)   # unicode的文本内容
        # self.log(response.body)     # 二进制内容
        #  {'download_timeout': 180.0, 'download_slot': 'ke.qq.com', 'download_latency': 0.592094898223877}
        # self.log(response.meta)
        # https://ke.qq.com/course/list?mt=1001&st=2002&tt=3019&price_min=1&page=1
        # self.log(response.url)
        # 保存下载的页面到文件，护或者到数据库（可以考虑文档数据库或者mysql关系数据库）
        # with open('page.html', 'w') as fd:
        #     fd.write(response.text)
        # 解析数据，并保存成csv文件。
        result = response.xpath('//section[1]/div/div[3]/ul/li')
        items = []  # 数据项数组列表
        for course_ in result:
            # self.log(type(course_))
            # # 课程名称
            # course_name = course_.xpath('h4[@class="item-tt"]/a/text()').get()
            # self.log('课程名称：{}'.format(course_name.strip() if course_name else ''))
            # # 培训机构
            # course_organization = course_.xpath(
            #     'div[@class="item-line item-line--middle"]/span[@class="item-source"]/a/text()').get()
            # self.log('培训机构：{}'.format(course_organization.strip() if course_organization else ''))
            # # 课程连接
            # course_link = course_.xpath('h4[@class="item-tt"]/a/@href').get()
            # self.log('课程连接：{}'.format(course_link.strip() if course_link else ''))
            # # 报名人数
            # course_number = course_.xpath(
            #     'div[@class="item-line item-line--middle"]/span[@class="line-cell item-user"]/text()').get()
            # self.log('报名人数：{}'.format(course_number.strip()  if course_number else ''))
            # # 课程状态
            # course_status = course_.xpath('div[@class="item-status"]/text()').get()
            # self.log('课程状态：{}'.format(course_status.strip() if course_status else ''))
            # # 课程价格
            # course_price = course_.xpath('div[@class="item-line item-line--bottom"]/span/text()').get()
            # self.log('课程价格：{}'.format(course_price.strip() if course_price else ''))
            # self.log('----------------------------')

            # 数据项
            item_ = ScraDataflowItem()
            course_name = course_.xpath('h4[@class="item-tt"]/a/text()').get()
            item_['course_name'] = '{}'.format(course_name.strip() if course_name else '')
            # 培训机构
            course_organization = course_.xpath(
                'div[@class="item-line item-line--middle"]/span[@class="item-source"]/a/text()').get()
            item_['course_organization'] = course_organization.strip() if course_organization else ''
            # 课程连接
            course_link = course_.xpath('h4[@class="item-tt"]/a/@href').get()
            item_['course_link'] = course_link.strip() if course_link else ''
            # 报名人数
            course_number = course_.xpath(
                'div[@class="item-line item-line--middle"]/span[@class="line-cell item-user"]/text()').get()
            item_['course_number'] = course_number.strip() if course_number else ''
            # 课程状态
            course_status = course_.xpath('div[@class="item-status"]/text()').get()
            item_['course_status'] = course_status.strip() if course_status else ''
            # 课程价格
            course_price = course_.xpath('div[@class="item-line item-line--bottom"]/span/text()').get()
            item_['course_price'] = course_price.strip() if course_price else ''
            items.append(item_)
        # 返回数据项到管道
        return items
