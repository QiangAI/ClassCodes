import http.server


class MyServer(http.server.HTTPServer):

    def process_request(self, request, client_address):
        print(self.request_queue_size)
        print('用户在请求：', client_address)
        print(type(request), request)
        while True:
            buf = request.recv(4 * 1024, 0)
            if not buf:
                break
            print(buf.decode('utf-8'))


server = MyServer(
    ('', 22222),  # 企业服务器只是某些ip开放
    RequestHandlerClass=None,
    bind_and_activate=True)

server.serve_forever()
