# coding = utf-8
import requests

session = requests.Session()
response = session.request(
    method='GET',
    url='http://www.baidu.com',
    params={'name': 'louis', 'age': 20})
print(type(response))
# print(response.content.decode('utf-8'))
print(response.status_code)
print(response.headers)
print(response.history)
