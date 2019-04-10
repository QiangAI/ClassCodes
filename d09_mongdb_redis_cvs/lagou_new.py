import json
import urllib.parse

import requests

# 宿主页面
url = 'https://www.lagou.com/jobs/list_%s?labelWords=&fromSearch=true&suginput='

url_home = url % urllib.parse.quote('算法工程师')
# 代理
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Safari/605.1.15',
}
# 请求session
session = requests.Session()
session.headers.update(headers)
# 首先访问宿主页面，获得cookie
r = session.get(url_home)

print(r.headers)
print(r.cookies)

# 更新Referer
session.headers.update({
    'Referer': url_home

})
print(session.headers)

# XHR请求
url_position = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
# 请求数据
data = {
    'first': False,
    'pn': 2,
    'kd': 'Python工程师'
}
print(session.cookies)
# 请求职位
response = session.post(
    url=url_position,
    data=data)
# 解析数据
json_content = json.loads(response.content)
print(json_content)
# 判定请求数据是否成功
if 'success' in json_content and json_content['success']:
    # 计算职位个数
    total_count = int(json_content['content']['positionResult']['totalCount'])
    print('总得职位数：', total_count)
    jobs = json_content['content']['positionResult']['result']
    for job in jobs:
        print(job)
