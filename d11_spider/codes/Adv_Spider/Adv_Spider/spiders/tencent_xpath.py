# -*- coding: utf-8 -*-
import scrapy


class TencentXpathSpider(scrapy.Spider):
    name = 'tencent_xpath'
    allowed_domains = ['ke.qq.com']
    start_urls = ['https://ke.qq.com/course/list?mt=1001&st=2002&tt=3019&price_min=1&page=1']

    def parse(self, response):
        selector = response.selector
        # print(selector.root.tag)  # 当前selector节点是html
        # # 节点名指定节点
        # nodename = selector.xpath('body')      # 当前html下的直系子节点
        # print(len(nodename), nodename)
        # nodename = selector.xpath('//div')  # html下的所有div子节点，包括孙子节点。
        # print(len(nodename))
        # nodename = selector.xpath('/html/body/header')  # 从根/开始的子节点（根式html）
        # print(len(nodename), nodename)
        # nodename = selector.xpath('.')  # 当前子节点
        # print(len(nodename), nodename)
        # nodename = selector.xpath('..')  # 上级子节点（这里返回[]）
        # print(len(nodename), nodename)
        #
        # nodename = selector.xpath('@lang')  # 返回lang属性的值
        # print(len(nodename), nodename)
        #
        # # 获取节点的值
        # print('获取节点值：', nodename.get())    # 第一个
        # print('获取节点值：', nodename.getall())  # 返回所有
        # 浏览器拷贝的xpath：/html/body/section[1]   # 有错误
        # nodes = response.xpath('/html/body//section')
        # print(len(nodes), nodes)
        # nodes = response.xpath('/html/body//section[1]')   # 位置从1开始
        # print(len(nodes), nodes)
        # nodes = response.xpath('/html/body//section[last()]')   # 最后位置，没有first
        # print(len(nodes), nodes)
        # nodes = response.xpath('/html/body//section[last()-1]')   # 以最后为坐标的相对位置
        # print(len(nodes), nodes)
        # nodes = response.xpath('/html/body//section[position()>=2]')  # 没有等于==，等于直接使用位置。
        # print(len(nodes), nodes)
        # nodes = response.xpath('/html/body//section[@class]')   # 含有属性
        # print(len(nodes), nodes)
        # nodes = response.xpath('/html/body//section[@class="main autoM clearfix"]')  # 属性等于值
        # print(len(nodes), nodes)
        # nodes = response.xpath('/html/body//section/div/div//ul/li/div[span]')   # 包含子节点
        # print('[span=]',len(nodes))
        # nodes = response.xpath('/html/body//section/div/div//ul/li/div[span="¥7280.00"]')  # 包含子节点的text节点为¥6800.00
        # print('[span=]', nodes)

        # nodes = response.xpath('/html/body//section/*')   # 所有section节点下的所有元素子节点
        # print('找到节点数：', len(nodes))
        #
        # nodes = response.xpath('/html/body//section/@*')  # 取出所有section的所有属性值
        # print(len(nodes), nodes)
        #
        # nodes = response.xpath('/html/body/node()')  # 取出所有类型的子节点
        # print('所有类型子节点：', len(nodes), nodes)
        # nodes = response.xpath('/html/body/*')  # 取出所有类型时元素（Element）的子节点
        # print('所有元素子节点:', len(nodes), nodes)
        # nodes = response.xpath('/html/body/text()')
        # print('所有文本子节点数：', len(nodes), nodes)

        # nodes = response.xpath('/html/body//section')
        # print('找到节点数：', len(nodes))
        # nodes = response.xpath('/html/body//header')
        # print('找到节点数：', len(nodes))
        #
        # nodes = response.xpath('/html/body//section|/html/body//header')
        # print('找到节点数：', len(nodes))

        # nodes = response.xpath('/html/body//section/ancestor::*')
        # print('ancestor：', len(nodes))  # html  body header  div
        #
        # nodes = response.xpath('/html/body//section/ancestor-or-self::*')
        # print('ancestor-or-self：', len(nodes))  # html  body header  div
        #
        # nodes = response.xpath('/html/body//section/attribute::*')
        # print('attribute：', len(nodes))  # html  body header  div
        #
        # nodes = response.xpath('/html/body//section/child::*')
        # print('child：', len(nodes))  # html  body header  div
        #
        # nodes = response.xpath('/html/body//section/descendant::*')
        # print('descendant：', len(nodes))  # html  body header  div
        #
        # nodes = response.xpath('/html/body//section/descendant-or-self::*')
        # print('descendant-or-self：', len(nodes))  # html  body header  div
        #
        # nodes = response.xpath('/html/body//section/following::*')
        # print('following：', len(nodes))  # html  body header  div
        # nodes = response.xpath('/html/body//section/following-sibling::*')
        # print('following-sibling：', len(nodes))  # html  body header  div
        # nodes = response.xpath('/html/body//section/namespace::*')
        # print('namespace：', len(nodes), nodes)  # html  body header  div
        #
        # nodes = response.xpath('/html/body//section/parent::*')
        # print('parent：', len(nodes), nodes)  # html  body header  div
        #
        # nodes = response.xpath('/html/body//section/preceding::*')
        # print('preceding：', len(nodes))  # html  body header  div
        #
        # nodes = response.xpath('/html/body//section/preceding-sibling::*')
        # print('preceding-sibling：', len(nodes))  # html  body header  div
        #
        # nodes = response.xpath('/html/body//section/self::section[@class="main autoM clearfix"]')
        # print('self：', len(nodes), nodes)  # html  body header  div

        # nodes = response.xpath('/html/body/comment()')
        # print('self：', len(nodes), nodes)  # 获取注释节点
        nodes = response.xpath('/html/body//section/div/div//ul/li/div/span[substring(text(),2)="7280.00"]/text()')
        print('self：', len(nodes), nodes)
