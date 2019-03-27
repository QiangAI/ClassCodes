# coding = utf-8
import requests
import requests.adapters
import requests.api


class MyAdapter(requests.adapters.BaseAdapter):
    def send(self, request, stream=False, timeout=None, verify=True,
             cert=None, proxies=None):
        print('在这儿做发送处理')
        print(type(request))
        print(dir(request))
        response = requests.api.get(url=request.url)
        return response  # 必须返回Response对象

    def close(self):
        print("close")


request = requests.Request(
    method='GET',
    url='http://www.baidu.com',
    params={'name': 'louis', 'age': 20})
pre_request = request.prepare()
session = requests.Session()
# 适配器
adapter = requests.adapters.HTTPAdapter(
    pool_connections=2,
    max_retries=3,
    pool_maxsize=10,
    pool_block=True)
adapter = MyAdapter()
# 挂在适配器
session.mount(prefix="http://", adapter=adapter)
# 只要前缀http://大头的请求都会试3次

response = session.send(pre_request)
print(response.status_code)
print(response.cookies)
