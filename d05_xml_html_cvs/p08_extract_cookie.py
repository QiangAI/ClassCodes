import http.cookiejar
import ssl
import urllib.request

"""
把请求cookie保存成文件
1. 发起请求
2. 得到响应
3. 利用CookieJar类提供函数，从Request，Response抽取Cookie
4. 保存Cookie
"""

# 4. 保存Cookie：利用FileCookieJar类或者子类

# 1. 发起请求urllib.request.openurl
request = urllib.request.Request(url='https://www.baidu.com')
# 2. 得到响应:上面的返回
response = urllib.request.urlopen(request, context=ssl._create_unverified_context())
# 3. 利用CookieJar类提供函数，从Request，Response抽取Cookie：利用构造器构造
cookies = http.cookiejar.MozillaCookieJar()
# cookies = http.cookiejar.MSIEDBCookieJar()
cookies.extract_cookies(response=response, request=request)

print(type(cookies))
for item_ in cookies:
    print(item_.name, item_.value, item_.path, item_.domain)

cookies.save('b.txt')
