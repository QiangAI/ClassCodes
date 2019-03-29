import http.server

server = http.server.HTTPServer(
    ('', 22222),
    RequestHandlerClass=http.server.SimpleHTTPRequestHandler,
    bind_and_activate=True)

print('启动http服务器')
# server.serve_forever()
server.handle_request()
print('服务器关闭')
