# coding = utf-8
import requests

request = requests.Request(
    method='GET',
    url='http://www.baidu.com',
    params={'name': 'louis', 'age': 20})
# pre_request = request.prepare()

# print(pre_request.url)
session = requests.Session()
pre_request = session.prepare_request(request)
response = session.send(pre_request)
# print(response.content.decode('utf-8'))
print(response.status_code)
print(response.headers)
print(response.history)
