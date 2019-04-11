# -*- coding: utf-8 -*-
import scrapy


class TencentSelectorSpider(scrapy.Spider):
    name = 'tencent_selector'
    allowed_domains = ['ke.qq.com']
    start_urls = ['https://ke.qq.com/course/list?mt=1001&st=2002&tt=3019&price_min=1&page=1']

    def parse(self, response):
        # scrapy.selector.unified.Selector
        # print(type(response))
        # print(type(response.selector))
        # content = response.body
        # print(type(content))
        # # 直接从response获取
        # selector_from_response = response.selector
        # # 使用response构造
        # selector_from_constructor = Selector(response=response)
        # # 使用text构造
        # selector_from_text = Selector(text=response.text, type='html')
        # # 使用root构造
        # selector_from_root = Selector(root=response.text.strip())
        #
        # # print(response.body)
        #
        # print(selector_from_constructor)
        # print(selector_from_response)
        # print(selector_from_text)
        # print(selector_from_root)
        #
        # print(selector_from_text.root)  # lxml.html.HtmlElement
        # print(type(selector_from_text._root))

        selector = response.selector
        # print(selector.response)
        # print(selector.attrib)
        # print(selector.namespaces)
        # print(selector.root)
        # print(selector._root)
        # # print(selector.text)
        # print(selector.type)
        # print(selector.selectorlist_cls)
        # print(selector.getall())
        # sel = selector.select('head')   # SelectorList
        # print(type(sel), sel)
        # pat = selector.xpath('head')     # SelectorList
        # print(type(pat), pat)
        # css = selector.css('head')     # SelectorList
        # print(type(css), css)
        #
        # # 注意：.不支持跨行匹配。
        # reg = selector.re(r'<head>([\s\S]*)</head>')   # list
        # print(type(reg), reg)

        # sel = selector.select('ul')   # SelectorList
        # print(len(sel), sel)
        # pat = selector.xpath('ul')     # SelectorList
        # print(len(pat), pat)
        # css = selector.css('ul')     # SelectorList
        # print(len(css), css)

        pat = selector.xpath('body/header')
        print(pat)
        for p in pat:
            element = p.root
            print(type(element), element)
            print(element.tag)  # 表签名
            print(element.base)  # base url
            print(element.base_url)  # 与上同
            print(element.attrib)  # 属性
            print(element.sourceline)  # 所在的行
            print(element.classes)  # classes属性的字符串集合封装
            print(element.text)  # 第一个子节点之前的文本
            for cls in element.classes:
                print(cls, type(cls))
            print(element.keys())  # 所有属性名
            print(element.values())  # 所有属性值
            # print(element.text_content())   # 节点值
            print(element.getchildren())  # 返回子节点
