# coding=utf-8
from scrapy.spiders import SitemapSpider


class TencentSitemapSpider(SitemapSpider):
    name = 'tencent_sitemap'

    # sitemap_urls = ['https://ke.qq.com/sitemap.xml']
    #
    # sitemap_rules = [
    #     (r'/course/list/','parse_list'),
    #     (r'/course/\d{6}','parse_course'),
    #     (r'/.*\.html','parse_index')
    #
    # ]
    #
    # sitemap_alternate_links=[]
    # #
    # # def parse(self, response):
    # #     print('默认处理：',response.url)
    #
    # def parse_list(self, response):
    #     print('课程列表：',response.url)
    #
    # def parse_course(self, response):
    #     print('课程信息：',response.url)
    #
    # def parse_index(self, response):
    #     print('目录主页：',response.url)
    #
    # def sitemap_filter(self, entries):
    #     lst_entries = list(entries)
    #     print('链接数:', len(lst_entries))
    #     # 只处理更新频率是：月（monthly）的页面
    #     for entry_ in lst_entries:
    #         if entry_['changefreq'] == 'monthly':
    #             yield entry_

    sitemap_urls = ['https://ke.qq.com/robots.txt']
    sitemap_follow = ['/dd/']
    sitemap_rules = [
        (r'/course/list/', 'parse_list'),
        (r'/course/\d{6}', 'parse_course')
    ]

    # def parse(self, response):
    #     print(response.url)

    def parse_list(self, response):
        print(type(response))
        print('课程列表：', response.url)

    def parse_course(self, response):
        print('课程信息：', response.url)
