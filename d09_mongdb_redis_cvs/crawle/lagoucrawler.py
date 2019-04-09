import json
import urllib.parse

import requests

"""
    功能：专门爬取拉勾的指定的职位信息
    作者：Louis Young
    日期：2019-04-08
"""

class LagouCrawler:

    def __init__(self):
        # 宿主页面url
        self.__url_home = 'https://www.lagou.com/jobs/list_%s?labelWords=&fromSearch=true&suginput='
        # 请求职位的url
        self.__url_position = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
        # 默认的头
        self.__agent = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
        }
        # 请求的数据体
        self.__data = {
            'first': True,
            'pn': 1,
            'kd': None
        }
        # 准备环境(使用session维护cookie与headers)
        self.__session = requests.Session()
        # 更新session的headers(存在就更新，不存在就添加)
        self.__session.headers.update(self.__agent)

    def get_jobs_count(self, job_name):
        """
        返回岗位数量
        :param job_name: 岗位名称
        :return:
        """
        # 更新session的头
        headers = {
            'Origin': 'https://www.lagou.com',
            'X-Anit-Forge-Code': '0',
            'X-Anit-Forge-Token': 'None',
            'X-Requested-With': 'XMLHttpRequest'
        }
        self.__session.headers.update(headers)
        # 1. 请求宿主页面（模拟浏览器的XHR行为：cookie）
        url_home = self.__url_home % urllib.parse.quote(job_name)
        r = self.__session.get(url_home)

        # 发起职位请求
        # 更新Referer头
        self.__session.headers.update({
            'Referer': url_home
        })
        # 更新请求的数据
        self.__data['pn'] = 1
        self.__data['first'] = True if self.__data['pn'] == 1 else False
        self.__data['kd'] = job_name

        response = self.__session.post(
            url=self.__url_position,
            data=self.__data)
        json_content = json.loads(response.content)
        if 'success' in json_content and json_content['success']:
            print('请求成功')
            total_count = int(json_content['content']['positionResult']['totalCount'])

            return total_count
        else:
            print('请求失败')
            return 0

    def crawle_page(self, no, job_name):
        """
        返回指定页面岗位数据
        :param no:
        :return:
        """
        # 更新请求的数据
        print(F'爬取开始：{no}')
        self.__data['pn'] = no
        self.__data['first'] = True if self.__data['pn'] == 1 else False
        self.__data['kd'] = job_name

        response = self.__session.post(
            url=self.__url_position,
            data=self.__data)
        json_content = json.loads(response.content)

        if 'success' in json_content and json_content['success']:
            # 解析数据
            pos_result = json_content['content']['positionResult']['result']
            return pos_result
        else:
            return []


    def close(self):
        print('爬虫关闭')
        self.__session.close()
