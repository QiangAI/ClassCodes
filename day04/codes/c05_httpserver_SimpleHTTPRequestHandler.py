# coding = utf-8
import http.server

print('启动服务器')
server = http.server.HTTPServer(
    server_address=('', 11111),
    RequestHandlerClass=http.server.SimpleHTTPRequestHandler,
    bind_and_activate=True)
print('接受用户请求')
server.serve_forever()
print('服务器退出')
