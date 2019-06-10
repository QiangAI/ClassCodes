# -*- coding: utf-8 -*-
import scrapy
from categories.items import CategoriesItem
from scrapy.http import Request


class CategoriesspiderSpider(scrapy.Spider):
    name = 'CategoriesSpider'
    allowed_domains = ['http://www.zgncpw.com']
    start_urls = ['http://www.zgncpw.com/']
    counter = 0

    # 启动爬取的首页
    def start_requests(self):
        for start_url in self.start_urls:  # 可以支持多个首页
            yield Request(
                url=start_url,
                callback=self.crawle_categories,
                method='GET',
                dont_filter=True)

    # 解析首页的农产品分类数据
    def crawle_categories(self, response):
        # 获取主菜单的农产品一级分类节点
        str_xpath = '//*[@id="top-menu"]/div/div/ul/li[@class="sub-menu pos-rel one"]/ul/li'
        all_categories = response.xpath(str_xpath)
        for categories in all_categories:
            # 解析出一级分类名
            category_type = categories.xpath('@title').get()
            # 循环解析二级分类节点
            type_categories = categories.xpath('ul/li')
            for category in type_categories:
                # 存放解析的一条数据
                item = CategoriesItem()
                # 一级分类名
                item['type'] = category_type
                # 二级分类名
                item['name'] = category.xpath('b/a/text()').get()
                # 二级分类的农产品销售信息页面链接URL
                item['url'] = category.xpath('b/a/@href').get()
                yield item
