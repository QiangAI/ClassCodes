import requests

session = requests.Session()
response = session.get('https://www.baidu.com')
print(type(response))
print(response.content.decode('utf-8'))
print(response.text)
print(response.__attrs__)
print(response.history)
