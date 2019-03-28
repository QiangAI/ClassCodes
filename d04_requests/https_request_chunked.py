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
ssl_sk.connect(('www.baidu.com', 443))

str_request = 'GET / HTTP/1.1\r\n'
str_request += F'Host: www.baidu.com\r\n'
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

# 解析分块数据Transfer-Encoding（分包）
regex = r'Transfer-Encoding: (.*)\r\n'
result = re.findall(regex, header_string, re.MULTILINE)
if result:
    # 读取数据的长度
    content_buffer = b''
    len_package = -1
    while len_package != 0:
        len_buffer = b''
        while True:
            buffer = ssl_sk.recv(1, 0)
            len_buffer += buffer
            last_two_bytes = len_buffer[-2:]
            if last_two_bytes == b'\r\n':
                print("数据包大小读取完毕")
                break
        print('长度内容:', len_buffer[:-2])
        len_package = int(len_buffer[:-2].decode('utf-8'), 16)
        print('数据包大小：', len_package)
        buffer = read_bytes(ssl_sk, len_package)
        print('读取的数据包大小:', len(buffer))
        content_buffer += buffer
        # 读取两个字节扔掉(\r\n)
        read_bytes(ssl_sk, 2)

    # 全部数据读取完毕
    print('--------------------')
    print(content_buffer.decode('utf-8'))
else:
    print('非分包数据')
