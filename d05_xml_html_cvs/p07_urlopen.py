import ssl
import urllib.request

request = urllib.request.Request('https://ke.qq.com',
                                 method='get',
                                 data=''.encode(),
                                 headers={})

# result = urllib.request.urlopen(
#     'http://www.huanqiu.com',
#     method='get',
#     data='',
#     headers={})
ctx = ssl._create_unverified_context()

result = urllib.request.urlopen('https://www.baidu.com', context=ctx)

# 判定request是字符串，直接使用某些参数，调用Request构造对象

print(result)  # http.client.HTTPResponse
print(result.status, result.reason)
print(result.headers)
print(result.read().decode('utf-8'))
