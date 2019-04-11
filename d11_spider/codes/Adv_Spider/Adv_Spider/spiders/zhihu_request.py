# -*- coding: utf-8 -*-
import hmac
import json
import time
from hashlib import sha1

import execjs
import scrapy


class ZhihuRequestSpider(scrapy.Spider):
    name = 'zhihu_request'
    allowed_domains = ['www.zhihu.com']
    start_urls = [
        'https://www.zhihu.com/signup?next=%2F',
        'https://www.zhihu.com/udid',
        'https://www.zhihu.com/api/v3/oauth/captcha?lang=en',
        'https://www.zhihu.com/api/v3/oauth/sign_in'
    ]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15',
        'content-type': 'application/x-www-form-urlencoded',
        'x-zse-83': '3_1.1'
    }

    def start_requests(self):
        # 发起第一个请求
        home_request = scrapy.Request(
            url=self.start_urls[0],
            callback=self.process_home,
            method='get',
            headers=self.headers,
            encoding='utf-8',
            priority=0,
            dont_filter=True,
            errback=self.handle_error
        )
        return [home_request]

    def handle_error(self, failure):
        print('处理错误', failure.getErrorMessage())
        print(failure.getTraceback())
        print(type(failure.value))
        print(type(failure.type))
        print(type(failure.stack))
        print(type(failure.frames))
        print(failure.value.response.status)
        print(failure.request)
        print(dir(failure))

    def process_home(self, response):
        # print(type(response))
        # print('url', response.url)
        # print('status', response.status)
        # print('headers', response.headers.getlist('Set-Cookie'))
        # print('flags', response.flags)
        # # print('body', response.body)
        # print('request', response.request)
        # # 主题request维护了cookie
        # print('request.cookies',response.request.cookies)
        # print('request.headers', response.request.headers)

        if response.status == 200:
            # for header_ in response.headers.items():
            #     print(header_)
            # print(response.headers['Set-Cookie'])
            # 请求成功，发起新的请求
            uuid_request = scrapy.Request(
                url=self.start_urls[1],
                callback=self.process_udid,
                # headers=self.headers,
                method='post',
                dont_filter=True,
                errback=self.handle_error
            )
            return [uuid_request]

    def process_udid(self, response):
        print('udid处理', response)
        if response.status == 200:
            print('查询校验码')
            is_captcha_request = scrapy.Request(
                url=self.start_urls[2],
                callback=self.query_is_captcha,
                headers=self.headers,
                method='get',
                dont_filter=True,
                errback=self.handle_error
            )
            return [is_captcha_request]

    def query_is_captcha(self, response):
        print('处理是否需要校验', response)
        print('状态码：', response.status)
        json_is_captcha = json.loads(response.body)
        if json_is_captcha['show_captcha']:
            print('下载校验码校验（put），并校验（post）')

        else:
            print('开始直接登录')
            print('发起登录请求')
            # 创建签名
            # 加密信息
            timestamp = str(int(time.time() * 1000))
            signature = self.get_signature(timestamp)
            encrypt = self.get_encrypt('13338629985', 'Louis123@yq', timestamp, signature, '')
            print(encrypt)
            data = encrypt

            # 数据没有采用字典，而是直接使用body

            login_request = scrapy.Request(
                url=self.start_urls[3],
                callback=self.process_login,
                headers=self.headers,
                method='post',
                body=data,
                dont_filter=True,
                errback=self.handle_error
            )
            return [login_request]

    def process_login(self, response):
        print('登录处理')
        print('登录状态：', response.status)

    # 签名函数
    def get_signature(self, now_):
        # 签名由clientId,grantType,source,timestamp四个参数生成
        h = hmac.new(
            key='d1b964811afb40118a12068ff74a12f4'.encode('utf-8'),
            digestmod=sha1)
        grant_type = 'password'
        client_id = 'c3cef7c66a1843f8b3a9e6a1e3160e20'
        source = 'com.zhihu.web'
        now = now_
        h.update((grant_type + client_id + source + now).encode('utf-8'))
        return h.hexdigest()

    # 提交信息加密函数
    def get_encrypt(self, username, password, timestamp, signature, captcha):
        str_login = ""
        str_login += "client_id=c3cef7c66a1843f8b3a9e6a1e3160e20&"
        str_login += "grant_type=password&"
        str_login += F"timestamp={timestamp}&"
        str_login += "source=com.zhihu.web"
        str_login += F"&signature={signature}&"
        str_login += F"username={username}&"
        str_login += F"password={password}&"
        str_login += F"captcha={captcha}&"
        str_login += "lang=en&"
        str_login += "ref_source=homepage&"
        str_login += "utm_source="

        with open('p05_custom_atob.js', 'r') as fd:
            js_zhihu = fd.read()

        ctx = execjs.compile(js_zhihu)
        encrypt_ = ctx.call('Q', str_login)
        return encrypt_
