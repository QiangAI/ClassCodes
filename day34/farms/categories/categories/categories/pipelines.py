# -*- coding: utf-8 -*-

import json

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from categories.dbs.redismq import RedisMQ


class CategoriesPipeline(object):
    redis_mq = RedisMQ()

    def process_item(self, item, spider):
        # 做一下简单的json格式处理
        content = json.dumps(dict(item), ensure_ascii=False)
        # 发送采集任务到队列
        self.redis_mq.push_task(content)
        return item
