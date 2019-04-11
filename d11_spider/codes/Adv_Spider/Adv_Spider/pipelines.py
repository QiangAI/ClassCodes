# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class AdvSpiderPipeline(object):
    def process_item(self, item, spider):
        # print(item,spider)
        return item


class ShowPipeline(object):

    def process_item(self, item, spider):
        # print('\t- show Pipeline:', item, spider)
        return item
