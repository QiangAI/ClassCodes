import http.client
import socket
import ssl


class MyConn(http.client.HTTPConnection):
    def connect(self):
        print('我们自己的链接')
        self.sock = ssl.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0))
        self.sock.connect((self.host, self.port))


conn = MyConn('www.baidu.com', 443)
# conn.request(
#     method='GET',
#     url='/',
#     body='kw=test',
#     headers={
#         'Accept-Encoding': 'identity',
#         'Content-Type': 'text/html;charset=utf-8'
#     })
conn.putrequest('GET', '/')
conn.putheader('Accept-Encoding', 'identity')
conn.putheader('Content-Type', 'text/html;charset=utf-8')
conn.endheaders()
conn.send('kw=test'.encode('utf-8'))
response = conn.getresponse()
print(type(response))
print(response.status, response.reason)
print(response.headers)
content = response.read()
print(content.decode())
conn.close()
