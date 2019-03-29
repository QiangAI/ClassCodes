import json
import ssl
import urllib.request


class BaiduHandler(urllib.request.BaseHandler):

    def default_open(self, req):
        req.add_header('Accept', 'application/json, text/javascript, */*; q=0.01')
        req.add_header('Connection', 'keep-alive')
        req.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
        req.add_header('Host', 'fanyi.baidu.com')
        req.add_header('User-Agent', 'Mozilla/5.0')


# a. 构造请求
request = urllib.request.Request(
    url='https://fanyi.baidu.com/sug',
    data='kw=test'.encode(),
    method='POST')

handler = BaiduHandler()
opener = urllib.request.build_opener(handler)

urllib.request.install_opener(opener)

response = urllib.request.urlopen(request, context=ssl._create_unverified_context())
# e. 发起请求
print(response.headers)
# eval
ct = response.read()
print(ct.decode('unicode-escape'))
re = json.loads(ct)
print(re)
