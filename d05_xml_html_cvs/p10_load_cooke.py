import http.cookiejar

cook = http.cookiejar.MozillaCookieJar('b.txt')
cook.load(ignore_discard=True, ignore_expires=True)
for item_ in cook:
    print(item_.name)
