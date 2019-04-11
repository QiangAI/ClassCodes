# -*- coding: utf-8 -*-
import scrapy


class TencentCssSpider(scrapy.Spider):
    name = 'tencent_css'
    allowed_domains = ['ke.qq.com']
    start_urls = ['https://ke.qq.com/course/list?mt=1001&st=2002&tt=3019&price_min=1&page=1']

    def parse(self, response):
        css = response.css('body')  # 元素选择器
        print(len(css), css)

        css = response.css('body > header.header-index')  # class选择器
        print(len(css), css)

        css = response.css('body > header#js_main_nav')  # id选择器
        print(len(css), css)

        css = response.css('''body 
             section.main.autoM.clearfix 
            > div 
            > div.market-bd.market-bd-6.course-list.course-card-list-multi-wrap.js-course-list 
            > ul 
            > li:nth-child(1) 
            > h4 
            > a::text''')  # body所有中所有section节点，包含孙子节点
        print(len(css), css)
        print(css.get())
        #
        # css = response.css('body')
        # print(len(css), css)
