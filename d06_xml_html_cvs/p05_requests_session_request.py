import requests

# session = requests.Session()
session = requests.session()  # 工厂模式
# response = session.request(
#     url='http://fy.webxml.com.cn/webservices/EnglishChinese.asmx/TranslatorString',
#     method='POST',
#     data=[('wordKey', 'handsome')],
#     headers={
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Safari/605.1.15'
#     }
# )

response = session.post(
    url='http://fy.webxml.com.cn/webservices/EnglishChinese.asmx/TranslatorString',
    data=[('wordKey', 'handsome')],
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Safari/605.1.15'
    }
)

print(response.text)
