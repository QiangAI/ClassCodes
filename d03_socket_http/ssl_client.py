import socket
import ssl

ip_addr = ('www.baidu.com', 443)

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)

sock = ssl.wrap_socket(sk)
sock.connect(ip_addr)

# sk.connect(ip_addr)

str_request = 'GET / HTTP/1.1\r\n'
str_request += F'Host: {ip_addr[0]}\r\n'
str_request += 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n'
str_request += 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Safari/605.1.15\r\n'
str_request += 'Accept-Language: zh-cn\r\n'
str_request += 'Connection: keep-alive\r\n'
str_request += '\r\n\r\n'

# 发送数据
sock.send(str_request.encode('utf-8'))

# 接收
while True:
    buf = sock.recv(4 * 1024, 0)
    if not buf:
        break
    print(buf.decode('utf-8'))
    # print(buf)
