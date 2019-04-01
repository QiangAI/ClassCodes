import requests.models

"""
method=None,  :方法请求get post
url=None,     :请求的url：  
headers=None, :请求头
cookies=None, :特殊的头（name=value，一堆的属性：过期属性，安全属性，domain属性，path属性等）
params=None,  :请求的querystring 

files=None,   |            |- multipart
data=None,    | - 构造body- |- form-urlencoding     只能三选一
json=None     |            |-  application/json

auth=None,    : 传递服务器登录信息
hooks=None,   : 与HTTP无关，编程模型的请求的回调（服务器相应后进行的处理）
                    |- 请求，响应分离处理
):

"""
# 1. 构造用户格式的请求
usr_request = requests.models.Request(
    method='POST',
    url='http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx/getMobileCodeInfo',
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Safari/605.1.15'
    },
    data=[('mobileCode', '13338629985'), ('userID', '')])

# 2. 编译成可以发送的请求
pre_request = usr_request.prepare()

# 3. 发送请求
session = requests.sessions.Session()
response = session.send(pre_request)
# 4. 处理请求
print(response.text)
