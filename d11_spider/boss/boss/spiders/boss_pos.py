# -*- coding: utf-8 -*-
import boss.items
import scrapy


class BossPosSpider(scrapy.Spider):
    name = 'boss_pos'

    page_no = 1
    # 3.1.的条件
    url_page = 'https://www.zhipin.com/c101010100/?query=%s&page=%d&ka=page-next'

    # 3.2.的条件header(设置到settings文件中)

    # 3. 重载爬虫的初始请求函数
    def start_requests(self):
        # 3.3.根据页数生成url
        url = self.url_page % (self.jobname, self.page_no)
        # 3.4. 创建请求对象
        request = scrapy.Request(
            url=url,
            method='get',
            callback=self.parse_pos,
            errback=self.parse_err,
            dont_filter=True)
        return [request]
        # yield request

    def parse_pos(self, response):
        print('抽取职位数据(数据抽取，是否继续爬取)')
        # 4.2. 找到职位节点
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
        url = self.url_page % (self.jobname, self.page_no)
        # 3.4. 创建请求对象
        request = scrapy.Request(
            url=url,
            method='get',
            callback=self.parse_pos,
            errback=self.parse_err,
            dont_filter=True)
        yield request

    def parse_err(self, error):
        print('处理爬取异常')
