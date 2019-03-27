import urllib.parse

url = 'http://joe:123456@www.baidu.com:80/download/pian.png?name=tom&page=2#anchor'
# url = 'file:///usr/local/python'
# url = 'ftp://joe:123456@www.baidu.com/download/pian.png?name=tom&page=2#anchor'
# universe resource locator
result = urllib.parse.urldefrag(url)
print(type(result), result.url, result.fragment)

re = urllib.parse.urlsplit(result.url)
print(re, type(re))

print(re.username)
print(re.password)
print(re.scheme)
print(re.netloc)
# print(re.password)
# print(re.password)
# print(re.password)
# print(re.password)
# print(re.password)
# print(re.password)
# print(re.password)
# print(re.password)
# print(re.password)

url_2 = 'http://www.baidu.com/index.html?name=帅哥&age=20'

r = urllib.parse.quote(url_2)
print(r)

rr = urllib.parse.unquote(r)
print(rr)
