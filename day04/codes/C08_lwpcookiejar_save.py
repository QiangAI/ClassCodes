# coding = utf-8
import http.client
import http.cookiejar
import urllib.request

host = 'http://www.baidu.com'
request = urllib.request.Request(url=host)
response = urllib.request.urlopen(request)

cookie = http.cookiejar.LWPCookieJar('a.txt')
# result = cookie.make_cookies(response, request)
cookie.extract_cookies(response, request)
cookie.save(ignore_discard=True, ignore_expires=True)
for item in cookie:
    # print(item)
    print(item.name, ':', item.value)
