# coding = utf-8
import http.server
import os


class MyHTTPHandler(http.server.BaseHTTPRequestHandler):

    def handle(self):
        print('request:', self.request)
        print('rfile:', self.rfile)
        # print('rfile:', self.rfile)
        # print('wfile:', self.wfile)
        # self.wfile.write('<h1>这是来自服务器的请求</h1>'.encode('utf-8'))  # 响应数据体
        # while True:
        #    buffer = self.request.recv(1024*4, 0)
        #    if not buffer:
        #        break;
        #    print(buffer.decode())
        while True:
            buffer = self.rfile.read(1024 * 4)
            if not buffer:
                break;
            print(buffer.decode())


print('方便kill进程的PID：', os.getpid())
print('启动服务器')
server = http.server.HTTPServer(
    server_address=('', 11111),
    RequestHandlerClass=MyHTTPHandler,
    bind_and_activate=True)
print('接受用户请求')
server.serve_forever()
print('服务器退出')
