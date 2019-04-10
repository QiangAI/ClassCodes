import time

import crawle.lagoucrawler
import crawle.mongostorage

"""
    使用Crawler与Storage实现岗位爬取与存储
"""


class LagouApp:

    def __init__(self, job_name):
        self.__job_name = job_name

        # 创建爬虫
        self.__crawler = crawle.lagoucrawler.LagouCrawler()
        # 创建存储
        self.__storage = crawle.mongostorage.MongoDBStorage()

    def crawle(self):
        print('开始爬取')
        # 获取岗位数量
        job_count = self.__crawler.get_jobs_count(self.__job_name)
        # 计算爬取的页数
        pages = 0
        if job_count % 15 == 0:
            pages = job_count // 15
        else:
            pages = job_count // 15
            pages += 1
        # 循环爬取每一页
        for no in range(1, pages):
            rows = self.__crawler.crawle_page(no, self.__job_name)
            print(rows)
            # 存储每一页
            self.__storage.add_rows(rows)
            time.sleep(10)

        self.__crawler.close()
        self.__storage.close()
