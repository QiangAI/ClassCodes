# -*- coding: utf-8 -*-
import json

import scrapy
import scrapy.http


class BaiduRequestSpider(scrapy.Spider):
    name = 'baidu_request'
    allowed_domains = ['fanyi.baidu.com']
    start_urls = ['https://fanyi.baidu.com/sug']

    def start_requests(self):
        # Request
        headers = {
            'content-type': 'application/x-www-form-urlencoded',
        }
        trnaslator_1 = scrapy.Request(
            url=self.start_urls[0],
            callback=self.get_translate,
            method='POST',  # 官方文档说需要大小，实际大小写都没有问题
            headers=headers,  # --> 指定表单格式
            dont_filter=True,  # 同一个请求url，防止被过滤
            body='kw=test'.encode())  # 使用body提交，必须手工指定表单格式

        # FormRequest
        form = {
            'kw': 'test'
        }
        trnaslator_2 = scrapy.FormRequest(
            url=self.start_urls[0],
            callback=self.get_translate,
            dont_filter=True,
            formdata=form)  # 不适合使用表单提交

        return [trnaslator_1, trnaslator_2]

    def get_translate(self, response):
        print('--------------------')
        result = json.loads(response.text)
        print(result)
