import http.server
import os


class FileHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        print(self.server)
        print(self.client_address)
        print(self.headers)
        print(self.command)
        print(self.path)
        self.send_response(200)  # 响应行
        self.send_header('Content-Type', 'text/html;charset=utf-8')  # 头
        self.end_headers()  # 空行
        print(type(self.wfile))
        self.wfile.write('<!doctype html>'.encode('utf-8'))
        self.wfile.write('<html>'.encode('utf-8'))
        self.wfile.write('<body>'.encode('utf-8'))
        files = os.listdir('.')
        for file in files:
            self.wfile.write(F'<a href="http://127.0.0.1:9898/">{file}</a><hr>'.encode('utf-8'))
        self.wfile.write('</body>'.encode('utf-8'))
        self.wfile.write('</html>'.encode('utf-8'))

    def do_POST(self):
        # 使用rfile读取请求提交的数据：form，multipart
        pass

    def do_INPUT(self):
        pass


# HTTPServer封装了基本的socket细节：socket创建，绑定，监听，接收
server = http.server.HTTPServer(
    ('', 9898),
    RequestHandlerClass=FileHandler,
    bind_and_activate=True)

server.serve_forever()
