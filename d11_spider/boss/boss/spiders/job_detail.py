# -*- coding: utf-8 -*-
import boss.items
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class JobDetailSpider(CrawlSpider):
    name = 'job_detail'
    allowed_domains = ['www.zhipin.com']
    page_no = 1
    url_page = 'https://www.zhipin.com/c101010100/?query=爬虫工程师&page=%d&ka=page-next'
    start_urls = [url_page % 1]

    rules = (
        Rule(LinkExtractor(
            allow=r'job_detail/.*\.html'),
            callback='parse_item',
            follow=True,
            process_links='pre_links'
        ),
    )

    def parse(self, response):
        list_jobs = response.xpath('//div[@class="job-list"]/ul/li')
        if len(list_jobs) == 0:
            return
        for job in list_jobs:
            # 4.3. 解析职位的数据
            item = boss.items.PositionItem()
            item['岗位名称'] = job.xpath('div/div/h3/a/div/text()').get()
            item['薪水'] = job.xpath('div/div/h3/a/span/text()').get()
            item['招聘机构'] = job.xpath('div/div/div/h3/a/text()').get()
            item['地区'] = job.xpath('div/div/p/text()').get()
            item['行业'] = job.xpath('div/div/div/p/text()').get()
            yield item
        # 4.4. 是否继续爬取
        self.page_no += 1
        url = self.url_page % self.page_no
        # 3.4. 创建请求对象
        request = scrapy.Request(
            url=url,
            method='get',
            callback=self.parse_pos,
            errback=self.parse_err,
            dont_filter=True)
        yield request


    def parse_item(self, response):
        print(response.url)
        # 处理response

    # def pre_links(self, list_links):
    #     print('处理')
    #     # 判定参数list_links是否是当前页面的链接，是就返回处理，不是，不处理\
    #     return  list_links
