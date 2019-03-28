import urllib.request


class MyHandler(urllib.request.BaseHandler):

    def default_open(self, req):
        print(req)
        print(type(req))
        print('用户在这里可以对request进行任何处理,比如Cookie的添加等')
        req.add_header('name', 'louis')  # 添加头，其他操作可以参考Request类


handler = MyHandler()
# 构建一个e处理器
opener = urllib.request.build_opener(handler)
# 安装一个Cookie处理器
urllib.request.install_opener(opener)

url = 'http://www.baidu.com'
request = urllib.request.Request(url=url, method='GET')
response = urllib.request.urlopen(url=request)
