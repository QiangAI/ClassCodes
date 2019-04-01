import requests

"""
'_content', 'status_code', 'headers', 'url', 'history',
        'encoding', 'reason', 'cookies', 'elapsed', 'request'
        
    raw
    

"""

# 请求
usr_request = requests.Request(
    url='http://fy.webxml.com.cn/webservices/EnglishChinese.asmx/TranslatorString',
    method='POST',
    data=[('wordKey', 'handsome')],
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Safari/605.1.15'
    })

# 编译请求
pre_request = usr_request.prepare()
# 发起请求
with requests.Session() as session:
    response = session.send(pre_request)
    # 处理响应xml（mp3文件base64加密）
    # print(response.text)    # 属性
    # print(response.raw)       # 成员变量
    # print(response.request)
    # print(response.status_code)
    # print(response.reason)
    # print(response.elapsed)
    # print(response.encoding)
    # print(response.history)
    # print(response.headers)
    # print(response.cookies)

    # it = response.iter_content(chunk_size=5, decode_unicode=True)
    # print(type(it))
    # for item_ in it:
    #     print(item_)

    lines = response.iter_lines(chunk_size=512)  # 解析行行呃呃时候，每次缓冲的大小，默认512。
    print(type(lines))
    for item_ in lines:
        print(item_)
