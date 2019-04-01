import requests.models

# https://ke.qq.com/course/list/python?price_min=1&page=4
# 1. 构造请求：get
# 1.1. 封装用户请求数据：Request
req = requests.models.Request(
    method='get',
    url='https://ke.qq.com/course/list/python',
    params={
        'price_min': 1,
        'page': 4},
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Safari/605.1.15'
    })  # 封装用户定位请求数据
# 构建成可以发送的请求：PreparedRequest
pre_req = req.prepare()  # 构造城标准的请求数据包
print(type(pre_req))
# 2. 发起请求
session = requests.sessions.Session()

response = session.send(pre_req)
print(response.text)
