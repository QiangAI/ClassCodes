# coding = utf-8
import http.cookies

cookies = http.cookies.BaseCookie('name=louis')
print(cookies)
print(type(cookies))
print(isinstance(cookies, dict))

re = cookies.value_decode('name=louis')
print(re)
re = cookies.value_encode('name=louis')
print(re)

cookies = http.cookies.SimpleCookie('name=louis')
print(cookies)
print(type(cookies))
print(isinstance(cookies, dict))

re = cookies.value_decode('name=louis')
print(re)
re = cookies.value_encode('name=louis')
print(re)
