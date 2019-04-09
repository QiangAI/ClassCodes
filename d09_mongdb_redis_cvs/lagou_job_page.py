# coding=utf-8
import codecs
import csv
import json

import requests

# 代理
ua_list =[
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6"]

# 构造请求数据
url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"
headers={
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Host': 'www.lagou.com',
    'Accept-Language': 'zh-cn',
    'Accept-Encoding': 'gzip, deflate',
    'Origin': 'https://www.lagou.com',
    'Referer': 'https://www.lagou.com/jobs/list_Python%E5%B7%A5%E7%A8%8B%E5%B8%88?labelWords=&fromSearch=true&suginput=',
    'User-Agent': ua_list[0],
#'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.1 Safari/605.1.15',
    'Connection': 'keep-alive',
    'Cookie': 'SEARCH_ID=b137bc127a5240b28e2a998056587686; TG-TRACK-CODE=index_search; JSESSIONID=ABAAABAABEEAAJA080B57268659EBB1C73E65E8835B1D1D; WEBTJ-ID=20181111160721-16701cf96c8949-0fc6f60feec025-48183706-1024000-16701cf96c94d2; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1541944837; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1541923641,1541944111; LGRID=20181111215853-ec514a2a-e5b9-11e8-9aa0-525400f775ce; LGSID=20181111214647-3bdcc9f7-e5b8-11e8-9a9f-525400f775ce; _ga=GA1.2.1318630155.1541923641; _gat=1; _gid=GA1.2.1216768844.1541923642; PRE_HOST=www.baidu.com; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpt_baidu_pc; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fs%3Fwd%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26rsv_spt%3D1%26rsv_iqid%3D0xf57dfecd000124aa%26issp%3D1%26f%3D8%26rsv_bp%3D1%26rsv_idx%3D2%26ie%3Dutf-8%26rqlang%3Dcn%26tn%3Dbaiduhome_pg%26rsv_enter%3D0%26oq%3Dpython%252520%2525E6%252595%2525B0%2525E6%25258D%2525AE%2525E6%25258C%252596%2525E6%25258E%252598%26rsv_t%3De111J%252FhqMM1XxboP3SPnY%252Fw6ah3WItaAjhCUX2DgoGHa814Syn2DSmf%252F0Kh31gQZTnH%252B%26inputT%3D6259%26rsv_pq%3D918956f400061b60%26rsv_sug3%3D280%26rsv_sug1%3D254%26rsv_sug7%3D100%26bs%3Dpython%2520%25E6%2595%25B0%25E6%258D%25AE%25E6%258C%2596%25E6%258E%2598; PRE_UTM=m_cf_cpt_baidu_pc; index_location_city=%E5%85%A8%E5%9B%BD; LGUID=20181111160538-9328c957-e588-11e8-9a22-525400f775ce; user_trace_token=20181111160538-9328c039-e588-11e8-9a22-525400f775ce',
    'X-Anit-Forge-Token': 'None',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Anit-Forge-Code': '0'
}

data={
    'first': False,
    'pn': 15,
    'kd': 'Python工程师'
}
session = requests.Session()
session.headers = headers

response = session.post(url, data=data)
result = json.loads(response.content.decode())
print(result)
# 解析数据，并保存呢
fields = ['工作年限', '学历', '职位', '薪水', '城市', '发布时间']
with open("jobs.csv", "w") as fd:
    fd.write(codecs.BOM_UTF8.decode())
    writer = csv.DictWriter(fd, fields, dialect="excel")
    writer.writeheader()
    postion = result["content"]["positionResult"]["result"]

    for item in postion:
        job = {
            '工作年限': item['workYear'],
            '学历': item['education'],
            '职位': item['positionName'],
            '薪水': item['salary'],
            '城市': item['city'],
            '发布时间': item['createTime']
        }
        writer.writerow(job)
