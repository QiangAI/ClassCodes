# coding = utf-8
import http.server
import os


class MyHTTPHandler(http.server.BaseHTTPRequestHandler):

    def handle(self):
        # super().handle()
        print('用户请求！')
        print('客户地址：', self.client_address)
        print('请求头：', self.headers)
        print('请求方法：', self.command)
        print('请求资源：', self.path)
        print('服务器socket：', self.server)
        print('HTTP版本：', self.server_version)
        self.send_response(200)  # 响应行
        self.send_header('Content-type', 'text/html;charset=utf-8')  # 响应头
        self.end_headers()  # 响应头结束
        self.wfile.write('<h1>这是来自服务器的请求</h1>'.encode('utf-8'))  # 响应数据体


print('方便kill进程的PID：', os.getpid())
print('启动服务器')
server = http.server.HTTPServer(
    server_address=('', 11111),
    RequestHandlerClass=MyHTTPHandler,
    bind_and_activate=True)
print('接受用户请求')
server.serve_forever()
print('服务器退出')
