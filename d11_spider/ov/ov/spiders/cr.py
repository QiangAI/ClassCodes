# -*- coding: utf-8 -*-
import scrapy


# scrapy crawl cr
# 引擎           爬虫
# 实例化spider的所有的Spdier子类或者Spider:对象池

# 1. 在对象池查找cr的对象，调用该对象的start_requests,还对象的返回Request对象，给引擎

# 引擎scrapy得到request，把request暂时存放在调度器，
# 等网络任务限制，从调度器取请求，发送给下载器，下载器直接下载网页，把结果返回给引擎。
# 引擎判定Request是否指定callback，直接调用，把下载结果传递给这个函数，
# 没有，直接调用parse，如果没有parse，报错。


class CrSpider(scrapy.Spider):
    # 1. 名字
    name = 'cr'
    allowed_domains = ['ke.qq.com']

    # 2. 重载start_requests函数（返回Request：url，method，callback）
    def start_requests(self):
        yield scrapy.Request(
            url='https://ke.qq.com',
            callback=self.handle_page,
            method='get')

    # 3. 处理数据
    def handle_page(self, reponse):
        print('处理数据')
        # return  [数据,Request]
