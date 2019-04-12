# -*- coding: utf-8 -*-
import scrapy
import scrapy.loader
import scrapy.loader.processors

class TencentItemSpider(scrapy.Spider):
    name = 'tencent_item'
    my_name = 'data'
    allowed_domains = ['ke.qq.com']
    start_urls = ['https://ke.qq.com/course/list?mt=1001&st=2002&tt=3019&price_min=1&page=1']

    def parse(self, response):
        # product = Product(name='Desktop PC',
        #                   price=1000,
        #                   last_updated='2019-03-13')
        #
        # print(product['last_updated'], product['name'])
        # print(product.get('name'))
        # print(product.get('stock', '缺省值'))
        # print('price' in product)
        # print('price' in product.fields)
        # print(1000 in product)
        # print(1000 in product.values())
        item = JobscrapyItem()
        # loader = scrapy.loader.ItemLoader(item=item,selector=response.selector)
        # loader = scrapy.loader.ItemLoader(item=item, response=response)

        # 测试xpath的代码
        # price = response.xpath('/html/body//section/div/div/ul/li/div/span[@class="line-cell item-price"]/text()')
        # print('self：', len(price), price.getall())
        # company_name = response.xpath('/html/body//section/div/div/ul/li/div/span/a/text()')
        # print('self：', len(company_name), company_name.getall())

        # course_list = response.xpath('/html/body//section[@class="main autoM clearfix"]/div/div/ul/li')
        # print(len(course_list))
        # for course_ in course_list:
        #     loader = scrapy.loader.ItemLoader(item=item, selector=course_, p5=50, p6=60)
        #     # loader.context={'p3': 10, 'p4': 20}
        #     # loader = CourseItemLoader(item=item, selector=course_)
        #     loader.add_xpath('company_name', 'div/span/a/text()')
        #     loader.add_xpath('course_price', 'div/span[@class="line-cell item-price"]/text()')
        #
        #     re = loader.get_xpath('div/span[@class="line-cell item-price"]/text()')
        #     # print(re)
        #     yield loader.load_item()

        course_list = response.xpath('/html/body//section[@class="main autoM clearfix"]/div/div/ul/li')
        print(len(course_list))
        for course_ in course_list:
            loader = scrapy.loader.ItemLoader(item=item, selector=course_)
            embeded_loader = loader.nested_xpath('div')
            embeded_loader.add_xpath('company_name', 'span/a/text()')
            embeded_loader.add_xpath('course_price', 'span[@class="line-cell item-price"]/text()')

            # embeded_loader.add_css()
            # embeded_loader.add_value()

            re = embeded_loader.get_xpath('span[@class="line-cell item-price"]/text()')
            # print(re)
            print(':', loader.load_item())
            yield loader.load_item()


#
# def in_price_processor(value):
#     print(float(value[0][1:]))
#     # print(value)
#     # 删除￥符号，转换为float类型
#     return float(value[0][1:])
#
#
# def out_price_processor(value):
#     print(value)
#     # 删除￥符号，转换为float类型
#     return value[0] + 100


def price_get_of_dollar(value, loader_context):
    # 去掉￥符号
    print('去掉￥符号：', value, loader_context)
    for it_ in loader_context.items():
        print('\t|- ', it_)
    return value[0][1:]


def to_float(value, loader_context):
    print('转换类型：', value, loader_context)
    for it_ in loader_context.items():
        print('\t|- ', it_)
    return float(value)


class JobscrapyItem(scrapy.Item):
    # 培训公司名
    company_name = scrapy.Field()
    # 课程价格
    course_price = scrapy.Field(
        # input_processor=in_price_processor,
        # output_processor = out_price_processor
        # input_processor = scrapy.loader.processors.Compose(price_get_of_dollar, to_float, p1=10, p2=20)
    )


# def price_processor(self, value):
#     print(self)   # 输出的类型是CourseItemLoader
#     print(float(value[0][1:]))
#     # print(value)
#     # 删除￥符号，转换为float类型
#     return float(value[0][1:])



def default_processor(self, value):
    print(value)
    return value[0]  # 传递的参数都是用[]列表


class CourseItemLoader(scrapy.loader.ItemLoader):
    # course_price_in = price_processor
    # course_price_out = price_processor
    # default_input_processor = default_processor
    # default_output_processor = default_processor
    course_price_in = scrapy.loader.processors.Compose(price_get_of_dollar, to_float, p1=10, p2=20)
