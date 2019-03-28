# coding = utf-8
import http.client
import http.cookiejar

cookie = http.cookiejar.MozillaCookieJar('a.txt', delayload=False)
cookie.load(ignore_discard=True, ignore_expires=True)
# 保存
'''
host = 'http://www.baidu.com'
request = urllib.request.Request(url=host)
response = urllib.request.urlopen(request)
cookie.extract_cookies(response, request)
cookie.save(ignore_discard=True, ignore_expires=True)
'''
for item in cookie:
    # print(item)
    print(item.name, ':', item.value)