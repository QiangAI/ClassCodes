import requests

session = requests.Session()

req1 = requests.Request(
    method='get',
    url='https://fanyi.baidu.com',
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Safari/605.1.15'}
)

pre_req1 = req1.prepare()

req2 = requests.Request(
    url='https://fanyi.baidu.com/sug',
    method='post',
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Safari/605.1.15'},
    data=[('kw', 'test')])
pre_req2 = req2.prepare()

# 输出观察：headers，cookies
# print(session.headers)
# print(session.cookies)
r1 = session.send(pre_req1)
# 输出观察：headers，cookies
# print(session.headers)
print(session.cookies)
print(r1.cookies)
# print(r1.request.cookies)
# print(r1.headers)
r2 = session.send(pre_req2)
# 输出观察：headers，cookies
# print(session.headers)
print(session.cookies)
print(r2.cookies)
# print(r2.headers)
# print(r2.request.cookies)
