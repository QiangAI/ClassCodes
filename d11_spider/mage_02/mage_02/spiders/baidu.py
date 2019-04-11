import scrapy

"""
scrapy爬虫引擎，调用爬虫程序，首先调用start_requests，其中返回的Request请求对象，
来决定我们需要爬取网站页面；

如果没有重载start_requests函数，他的默认实现：是从start_urls种循环获取爬取的页面url

|- 提供start_urls
|- 重载start_requests函数
"""


class BaiduSpider(scrapy.Spider):
    name = 'baidu'

    def parse1(self, response):
        print('数据处理，默认函数')
        self.log('日志输出')
        print(response.body)

    def handle_data(self, response):
        print('绑定处理函数 自己的函数')
        print(type(response))
        print(response.text)

    def start_requests(self):
        print('开发爬虫')
        return [
            scrapy.Request('http://www.huanqiu.com', callback=self.handle_data),
            scrapy.Request('https://ke.qq.com', callback=self.parse1),
            scrapy.Request('https://ke.qq.com', dont_filter=True, callback=self.parse1),
        ]
