# coding = utf-8
import http.cookies

cookies = http.cookies.SimpleCookie('name=louis')
cookies['pass'] = 'tom123'
cookies.load('work=swim')
print(cookies.output())
out = cookies.output()
print(type(out))
print(out.encode('utf-8'))
