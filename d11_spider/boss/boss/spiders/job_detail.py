# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class JobDetailSpider(CrawlSpider):
    name = 'job_detail'
    allowed_domains = ['www.zhipin.com']
    start_urls = ['https://www.zhipin.com/c101010100/?query=爬虫工程师&page=3&ka=page-next']

    rules = (
        Rule(LinkExtractor(
            allow=r'job_detail/.*\.html'),
            callback='parse_item',
            follow=True,
            process_links='pre_links'
        ),
    )

    def parse(self, response):
        print('结果', response.url)
        # 抽取response职位（岗位名，薪水，地区，.....,职位描述没有，通过超链接爬取）

        # 抽取链接,形成列表

        return super().parse(response)

    def parse_item(self, response):
        print(response.url)
        # 处理response

    def pre_links(self, list_links):
        print('处理')
        # 判定参数list_links是否是当前页面的链接，是就返回处理，不是，不处理
