import requests
import requests.adapters


class MyAdapter(requests.adapters.BaseAdapter):
    def send(self, request, stream=False, timeout=None, verify=True,
             cert=None, proxies=None):
        print(type(request))
        print('对某些特殊的url进行独立的处理')
        if request.method.upper() == 'GET':
            resp = requests.api.get(request.url)
        else:
            resp = None
        return resp


session = requests.Session()
adapter = MyAdapter()

session.mount('https://', adapter=adapter)

response = session.get(
    url='https://www.baidu.com',
    headers={'Content-Type': 'text/html;charset=UTF-8'})
print(response.content.decode('utf-8'))
