import http
import http.cookies
import http.server


class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # print(self.client_address)
        # print(self.headers)
        if 'Cookie' in self.headers:
            ck = http.cookies.BaseCookie(self.headers['Cookie'])

        ck2 = http.cookies.BaseCookie('name=louis; age=20')

        # print(self.command)
        # print(self.server)
        self.send_response(200)  # 构造响应行
        self.send_header('Content-type', 'text/html;charset=utf-8')
        self.send_header(ck2.output())

        self.end_headers()  # 构造响应头
        self.wfile.write('<h1>大家好</h1>'.encode('utf-8'))  # 构造响应体

        # 客户端的头能够得到
        # 客户端的方法
        # 客户端的体


server = http.server.HTTPServer(
    ('', 22222),
    RequestHandlerClass=MyHandler,
    bind_and_activate=True)

print('启动http服务器')
server.serve_forever()
# server.handle_request()
print('服务器关闭')
