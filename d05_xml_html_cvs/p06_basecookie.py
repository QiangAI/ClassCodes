import http.cookies

ck = http.cookies.BaseCookie('name=Louis')
ck['age'] = 20
ck['favor'] = 'Travel'

for k, v in ck.items():
    print(k, v)

print(ck.output())
