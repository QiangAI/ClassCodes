# coding = utf-8
import requests

request = requests.Request(
    method='GET',
    url='http://www.baidu.com',
    params={'name': 'louis', 'age': 20})
pre_request = request.prepare()
session = requests.Session()
print(session.cookies)
print(session.headers)

response = session.send(pre_request)
print(session.cookies)
print(session.headers)
print(response.cookies)
response = session.send(pre_request)
print(session.cookies)
print(session.headers)
print(response.cookies)
