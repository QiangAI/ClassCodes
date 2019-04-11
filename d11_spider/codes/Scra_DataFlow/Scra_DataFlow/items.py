# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScraDataflowItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 课程名称
    course_name = scrapy.Field()
    # 培训机构
    course_organization = scrapy.Field()
    # 课程连接
    course_link = scrapy.Field()
    # 报名人数
    course_number = scrapy.Field()
    # 课程状态
    course_status = scrapy.Field()
    # 课程价格
    course_price = scrapy.Field()
