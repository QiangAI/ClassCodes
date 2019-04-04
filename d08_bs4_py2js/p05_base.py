import base64

result = base64.b64encode('abcdefghfgdggdgdg'.encode('utf-8'))
print(result)

resu = base64.b64decode(result)
print(resu)
