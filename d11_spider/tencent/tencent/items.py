# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    org = scrapy.Field()
    price = scrapy.Field()


class NonFee(scrapy.Item):
    pass
