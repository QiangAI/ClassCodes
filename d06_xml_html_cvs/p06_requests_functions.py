import requests

response = requests.get(
    url='https://ke.qq.com/course/list/python',
    params={'price_min': 1, 'page': 2},
    headers={
        'User-Agent': 'Mozilla/5.0'
    })

print(response.text)
