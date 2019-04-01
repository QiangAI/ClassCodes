import requests.models

# 构造请求
pre = requests.models.PreparedRequest()
# pre.prepare_method('get')
# pre.prepare_url(
#     url='https://ke.qq.com/course/list/python',
#     params={
#         'price_min': 1,
#         'page': 4
#     }
# )
# pre.prepare_headers(
#     headers={
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Safari/605.1.15'
#     }
# )
pre.prepare(
    method='get',
    url='https://ke.qq.com/course/list/python',
    params={
        'price_min': 1,
        'page': 4},
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Safari/605.1.15'
    }
)

# 发送请求
session = requests.sessions.Session()

response = session.send(pre)
print(response.text)
