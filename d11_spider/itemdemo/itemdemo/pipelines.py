# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ItemdemoPipeline(object):
    def process_item(self, item, spider):
        # 链接Redis
        # 找到数据库
        # 数据存储
        # print('Redis CSV数据项的最终处理',item)
        return item


class MongoDBPipeline(object):
    def process_item(self, item, spider):
        # print('MonfgoDB存储')

        return item
