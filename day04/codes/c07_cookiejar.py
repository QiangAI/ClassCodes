# coding = utf-8
import http.client
import http.cookiejar
import urllib.request

host = 'http://www.baidu.com'
request = urllib.request.Request(url=host)
response = urllib.request.urlopen(request)

cookie = http.cookiejar.CookieJar()
# result = cookie.make_cookies(response, request)
cookie.extract_cookies(response, request)

for item in cookie:
    # print(item)
    print(item.name, ':', item.value)

