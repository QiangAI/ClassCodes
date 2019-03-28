import re
import socket
import ssl


def read_bytes(s, size):
    buffer_ = b''
    len_ = size
    while len_ != 0:
        buf = s.recv(len_, 0)
        buffer_ += buf
        len_ -= len(buf)
    return buffer_

"""
def wrap_socket(sock, keyfile=None, certfile=None,
                server_side=False, cert_reqs=CERT_NONE,
                ssl_version=PROTOCOL_TLS, ca_certs=None,
                do_handshake_on_connect=True,
                suppress_ragged_eofs=True,
                ciphers=None):
"""

# 创建socket
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
# 使用ssl包装socket
ssl_sk = ssl.wrap_socket(sk)

# 链接到https://www.baidu.com
ssl_sk.connect(('ke.qq.com', 443))

str_request = 'GET / HTTP/1.1\r\n'
str_request += F'Host: ke.qq.com\r\n'
str_request += 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n'
str_request += 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Safari/605.1.15\r\n'
str_request += 'Accept-Language: zh-cn\r\n'
str_request += 'Connection: Close\r\n'
str_request += '\r\n\r\n'

ssl_sk.send(str_request.encode('utf-8'), 0)

# 读取响应行，响应头，空行
# 接受头（获取数据的长度）
header_buffer = b''
while True:
    buffer = ssl_sk.recv(1, 0)
    header_buffer += buffer
    last_four_bytes = header_buffer[-4:]
    if last_four_bytes == b'\r\n\r\n':
        print("头读取完毕")
        break
# 处理头
header_string = header_buffer.decode('utf-8')
print('头：\n', header_string)
regex = r'Content-Length: (\d*?)\r\n'
len_content = re.findall(regex, header_string, re.MULTILINE)
if len_content:
    len_content = int(len_content[0], 10)
    print('数据包长度:', len_content)
    content_buffer = read_bytes(ssl_sk, len_content)
    print('读取的数据包大小：', len(content_buffer))
    print('-----------------------')
    print(content_buffer.decode('utf-8'))
