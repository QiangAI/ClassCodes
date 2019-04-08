import json

import requests

"""
    功能：专门爬取拉勾的指定的职位信息
    作者：Louis Young
    日期：2019-04-08
"""


class LagouCrawler:

    def __init__(self):
        self.__url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
        self.__headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Safari/605.1.15',
            'Host': 'www.lagou.com',
            'Origin': 'https://www.lagou.com',
            'X-Anit-Forge-Token': 'None',
            'X-Requested-With': 'XMLHttpRequest',
            'X-Anit-Forge-Code': '0',
            'Cookie': 'SEARCH_ID=4a039a1e18f5463eb35dd6ee73c9ba1d; TG-TRACK-CODE=index_search; JSESSIONID=ABAAABAAAIAACBI902A58126CD17B53215E5B278040E5EF; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1554718011; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1553765196,1554714486,1554717281; LGRID=20190408180651-078a5476-59e6-11e9-9b50-525400f775ce; LGSID=20190408175500-5fe74e79-59e4-11e9-8cd1-5254005c3644; X_HTTP_TOKEN=af28af7ea1cca126110817455133c3bfd7bd85fd32; _ga=GA1.2.1431561226.1553765197; _gat=1; _gid=GA1.2.605634441.1554714487; PRE_HOST=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%25E7%25AE%2597%25E6%25B3%2595%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588%3FlabelWords%3D%26fromSearch%3Dtrue%26suginput%3D; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Futrack%2FtrackMid.html%3Ff%3Dhttps%253A%252F%252Fwww.lagou.com%252Fjobs%252Flist_%2525E7%2525AE%252597%2525E6%2525B3%252595%2525E5%2525B7%2525A5%2525E7%2525A8%25258B%2525E5%2525B8%252588%253FlabelWords%253D%2526fromSearch%253Dtrue%2526suginput%253D; PRE_UTM=; X_MIDDLE_TOKEN=63756adeba54be9eb026b66135fd1087; index_location_city=%E5%85%A8%E5%9B%BD; LGUID=20190328172637-961e233f-513b-11e9-b829-5254005c3644; user_trace_token=20190328172637-961e2008-513b-11e9-b829-5254005c3644'
        }
        self.__data = {
            'first': False,
            'pn': 1,
            'kd': '算法工程师'
        }
        self.__session = requests.Session()

    def get_jobs_count(self, job_name):
        """
        返回岗位数量
        :param job_name: 岗位名称
        :return:
        """
        self.__data['first'] = True
        self.__data['pn'] = 1
        self.__data['kd'] = job_name

        # 构造器请求,# 发起请求
        resp = self.__session.get(url='https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=')
        print(self.__session.cookies)
        print(resp.cookies)
        response = self.__session.post(url=self.__url, data=self.__data, headers=self.__headers)
        json_content = json.loads(response.content)
        print(json_content)

        return 0

    def crawle_page(self, no, job_name):
        """
        返回指定页面岗位数据
        :param no:
        :return:
        """
        print(F'爬取开始：{no}')
        return []

    def close(self):
        print('爬虫关闭')
