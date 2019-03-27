import http.cookiejar
import urllib.request

# url = 'http://127.0.0.1:9999'    # 可以自己写一个Web服务器，来接受这里发送的数据
url = 'http://www.baidu.com'
request = urllib.request.Request(url=url, data='hello'.encode('utf-8'), method='GET')
# 默认的都是GET方法，所以不需要data参数，对一般的请求，也不需要使用证书。
response = urllib.request.urlopen(url=request, data='world'.encode('utf-8'))
print(type(response))

# 返回的是http.client.HTTPResponse对象。
# 头
print(response.headers)
# 响应行
print(response.status)
print(response.reason)
# 读取内容
# print(response.read())

# 注意：urlopen中的data会覆盖Request中定义的data
# 创建Cookie处理数据对象
cookie = http.cookiejar.CookieJar()
# 创建一个Cookie处理器
handler = urllib.request.HTTPCookieProcessor(cookie)
