import json
import ssl
import urllib.request

# a. 构造请求
request = urllib.request.Request(
    url='https://fanyi.baidu.com/sug',
    data='kw=test'.encode(),
    headers={
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'fanyi.baidu.com',
        'User-Agent': 'Mozilla/5.0',
    },
    method='POST')

response = urllib.request.urlopen(request, context=ssl._create_unverified_context())
# e. 发起请求
print(response.headers)
# eval
ct = response.read()
print(ct.decode('unicode-escape'))
re = json.loads(ct)
print(re)
