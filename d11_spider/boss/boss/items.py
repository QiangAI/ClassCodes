# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# 4.1 定义爬取的字段
class PositionItem(scrapy.Item):
    # 定义数据字段
    岗位名称 = scrapy.Field()
    薪水 = scrapy.Field()
    招聘机构 = scrapy.Field()
    地区 = scrapy.Field()
    行业 = scrapy.Field()
