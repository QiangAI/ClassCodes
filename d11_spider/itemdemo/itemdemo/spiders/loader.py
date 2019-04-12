# -*- coding: utf-8 -*-
import scrapy
import scrapy.loader


class LoaderSpider(scrapy.Spider):
    name = 'loader'
    allowed_domains = ['ke.qq.com']
    url = 'https://ke.qq.com/course/list/Python开发?page=1'

    def start_requests(self):
        request = scrapy.Request(url=self.url, callback=self.item_handle)
        yield request

    def item_handle(self, response):
        print("------------")
        # 定位处理的节点
        course_list = response.xpath('//div[@data-report-module="middle-course"]/ul/li')
        # 循环处理课程
        for course in course_list:
            # item对象
            item = CourseItem()
            # 定义加载器
            loader = scrapy.loader.ItemLoader(item=item, selector=course)
            # loader = CourseItemLoader(item=item, selector=course)
            # loader.nested_xpath('div')
            loader.context = {'p1': 20, 'p2': 30}
            # 添加xpath，或者 Css 或者value
            loader.add_xpath('机构名称', 'div/span/a/text()')
            # loader.add_css('课程名称', 'h4 > a::text')
            loader.add_xpath('学习人数', 'div[@class="item-line item-line--middle"]/span/text()')
            loader.add_css('课程价格', 'div[class="item-line item-line--bottom"] > span::text')
            # loader.add_value('课程价格', '8888')
            # 返回数据
            yield loader.load_item()


def in_handle(value):
    print('数据输入细节处理')
    if value[0] == '免费':
        return value[0]
    else:
        return value[0][1:]


def out_handle(value):
    print('数据输出细节处理', value)
    return value[0]


class CourseItem(scrapy.Item):
    机构名称 = scrapy.Field()
    课程名称 = scrapy.Field()
    学习人数 = scrapy.Field()
    课程价格 = scrapy.Field(
        # input_processor=in_handle, output_processor=out_handle
    )
#
# # 成员函数
# def xxx(self, value, loader_context):
#     print('人数处理-前', value)
#
#     print(loader_context)
#     return value


# def yyy(self, value, loader_context):
#     print('人数处理-后')
#     return value
#
# class YYY:
#     def __call__(self, value, loader_context):
#         print('人数处理-后')
#         return value
#
#
#
# class CourseItemLoader(scrapy.loader.ItemLoader):
#     # 字段名_in
#     # 字段名_out
#
#     学习人数_in = YYY
#     学习人数_out = scrapy.loader.processors.TakeFirst
