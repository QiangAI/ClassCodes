# coding = utf-8
import requests


def my_hook(response, *args, **kwargs):
    print(response)
    print('hook处理')
    print(len(args))
    print(len(kwargs))
    print(kwargs)


request = requests.Request(
    method='GET',
    url='http://www.baidu.com',
    params={'name': 'louis', 'age': 20},
    hooks=dict(response=my_hook))

pre_request = request.prepare()

session = requests.Session()
response = session.send(pre_request)

