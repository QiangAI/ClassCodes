# coding = utf-8
import http.cookiejar

cookie = http.cookiejar.LWPCookieJar('a.txt', delayload=False)
cookie.load(ignore_discard=True, ignore_expires=True)
for item in cookie:
    # print(item)
    print(item.name, ':', item.value)
