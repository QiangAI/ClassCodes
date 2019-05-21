# coding=utf-8
import codecs
import csv
import json
import random
import time

import requests


def add2File(data):
    fields = ['工作年限', '学历', '职位', '职位ID', '薪水', '城市', '发布时间']
    with open("jobs.csv", "a") as fd:
        # fd.write(codecs.BOM_UTF8.decode())
        writer = csv.DictWriter(fd, fields, dialect="excel")
        job = {
            '工作年限': data[0],
            '学历': data[1],
            '职位': data[2],
            '职位ID': data[3],
            '薪水': data[4],
            '城市': data[5],
            '发布时间': data[6]
        }
        writer.writerow(job)


class LagouCrawler:
    url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Host': 'www.lagou.com',
        'Accept-Language': 'zh-cn',
        'Accept-Encoding': 'gzip, deflate',
        'Origin': 'https://www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_Python%E5%B7%A5%E7%A8%8B%E5%B8%88?labelWords=&fromSearch=true&suginput=',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.1 Safari/605.1.15',
        'Connection': 'keep-alive',
        'Cookie': 'SEARCH_ID=b137bc127a5240b28e2a998056587686; TG-TRACK-CODE=index_search; JSESSIONID=ABAAABAABEEAAJA080B57268659EBB1C73E65E8835B1D1D; WEBTJ-ID=20181111160721-16701cf96c8949-0fc6f60feec025-48183706-1024000-16701cf96c94d2; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1541944837; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1541923641,1541944111; LGRID=20181111215853-ec514a2a-e5b9-11e8-9aa0-525400f775ce; LGSID=20181111214647-3bdcc9f7-e5b8-11e8-9a9f-525400f775ce; _ga=GA1.2.1318630155.1541923641; _gat=1; _gid=GA1.2.1216768844.1541923642; PRE_HOST=www.baidu.com; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpt_baidu_pc; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fs%3Fwd%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26rsv_spt%3D1%26rsv_iqid%3D0xf57dfecd000124aa%26issp%3D1%26f%3D8%26rsv_bp%3D1%26rsv_idx%3D2%26ie%3Dutf-8%26rqlang%3Dcn%26tn%3Dbaiduhome_pg%26rsv_enter%3D0%26oq%3Dpython%252520%2525E6%252595%2525B0%2525E6%25258D%2525AE%2525E6%25258C%252596%2525E6%25258E%252598%26rsv_t%3De111J%252FhqMM1XxboP3SPnY%252Fw6ah3WItaAjhCUX2DgoGHa814Syn2DSmf%252F0Kh31gQZTnH%252B%26inputT%3D6259%26rsv_pq%3D918956f400061b60%26rsv_sug3%3D280%26rsv_sug1%3D254%26rsv_sug7%3D100%26bs%3Dpython%2520%25E6%2595%25B0%25E6%258D%25AE%25E6%258C%2596%25E6%258E%2598; PRE_UTM=m_cf_cpt_baidu_pc; index_location_city=%E5%85%A8%E5%9B%BD; LGUID=20181111160538-9328c957-e588-11e8-9a22-525400f775ce; user_trace_token=20181111160538-9328c039-e588-11e8-9a22-525400f775ce',
        'X-Anit-Forge-Token': 'None',
        'X-Requested-With': 'XMLHttpRequest',
        'X-Anit-Forge-Code': '0'
    }
    data = {
        'first': True,
        'pn': 1,
        'kd': 'Python开发工程师'
    }

    def __init__(self):
        # 链接环境
        self.session = requests.Session()
        self.session.headers = self.headers

    def crawl(self, isfirst, pagenum):
        # 爬取
        self.data['first'] = isfirst
        self.data['pn'] = pagenum
        # 更换代理
        response = self.session.post(self.url, data=self.data)
        content = json.loads(response.content.decode())
        if response.status_code == 200 and "content" in content:
            result = content['content']['positionResult']
            if isfirst:
                self.total = result['totalCount']
                self.pagesize = result['resultSize']
            position = result['result']
            for item in position:
                data = []
                data.append(item['workYear'])
                data.append(item['education'])
                data.append(item['positionName'])
                data.append(item['positionId'])
                data.append(item['salary'])
                data.append(item['city'])
                data.append(item['createTime'])
                add2File(data=data)
            return True
        else:
            return False


fields = ['工作年限', '学历', '职位', '职位ID', '薪水', '城市', '发布时间']
with open("jobs.csv", "a") as fd:
    fd.write(codecs.BOM_UTF8.decode())
    writer = csv.DictWriter(fd, fields, dialect="excel")
    writer.writeheader()
crawler = LagouCrawler()
crawler.crawl(True, 1)

# pages=crawler.total//crawler.pagesize+1
# print("一共有%d职位，页数:%d"%(crawler.total,pages))
for i in range(2, 180):
    print("爬取第%0d页" % (i))
    re = crawler.crawl(False, i)
    if not re:
        print("爬取异常，中断爬取进程！")
        break
    time.sleep(random.uniform(10, 15))
