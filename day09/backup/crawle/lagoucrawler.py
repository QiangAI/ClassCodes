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
        # 职位的xhr请求url
        self.__url_position = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
        # 职位的宿主页面
        self.__url = 'https://www.lagou.com/jobs/list_%s?labelWords=&fromSearch=true&suginput='
        # 浏览器代理
        self.__agent = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Safari/605.1.15',
        }
        # 职位请求的数据体
        self.__data = {
            'first': True,
            'pn': 1,
            'kd': None
        }
        # 用来维护会话
        self.__session = requests.Session()
        # 更新session的header代理
        self.__session.headers.update(self.__agent)

    def get_jobs_count(self, job_name):
        """
        返回岗位数量
        :param job_name: 岗位名称
        :return:
        """
        # 数据初始化
        self.__data['first'] = True
        self.__data['pn'] = 1
        self.__data['kd'] = job_name
        # 根据职位，构造宿主页面
        url_home = self.__url % urllib.parse.quote(job_name)
        # 发起对宿主页面的请求，获取Cookie
        self.__session.get(url=url_home)
        # 更新新的请求的Referer请求
        self.__session.headers.update({
            'Referer': url_home
        })
        # 发起对第一页职位数据请求，获得职位数
        response = self.__session.post(url=self.__url_position, data=self.__data)
        # 解析数据
        json_content = json.loads(response.content)
        # 判定请求数据是否成功
        if 'success' in json_content and json_content['success']:
            # 计算职位个数
            total_count = int(json_content['content']['positionResult']['totalCount'])
            print('总的职位数：', total_count)
            return total_count
        else:
            print('请求错误')
            return 0

    def crawle_page(self, no, job_name):
        """
        返回指定页面岗位数据
        :param no:
        :return:
        """
        print(F'爬取开始：{no}')
        # 数据初始化
        self.__data['first'] = True if no == 1 else False
        self.__data['pn'] = no
        self.__data['kd'] = job_name

        # 发起对第一页职位数据请求，获得职位数
        response = self.__session.post(url=self.__url_position, data=self.__data)
        # 解析数据
        json_content = json.loads(response.content)
        # 判定请求数据是否成功
        if 'success' in json_content and json_content['success']:
            # 计算职位个数
            pos_result = json_content['content']['positionResult']['result']
            # 解析数据
            return pos_result
        else:
            return None

    def close(self):
        print('爬虫关闭')
        self.__session.close()
