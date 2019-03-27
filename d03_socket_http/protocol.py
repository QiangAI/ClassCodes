# coding = utf-8
import re
import socket

server_name = 'www.baidu.com'

# 把域名转换成IP
list_info = socket.getaddrinfo(
    host=server_name,
    port=80,
    family=socket.AF_INET,
    type=socket.SOCK_STREAM,
    proto=socket.IPPROTO_TCP,
    flags=socket.AI_ALL)
for _, _, _, _, address in list_info:
    print("IP:%s,PORT:%d" % address)

# 创建socket
client_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
    socket.IPPROTO_TCP)

# 使用服务器IP，连接到服务器
print(list_info[0][-1])
client_socket.connect(list_info[0][-1])
# 构造Request头（HTTP协议）
request_string = ''
request_string += 'GET / HTTP/1.1\r\n'
request_string += 'Host: %s:80\r\n' % server_name
request_string += 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n'
request_string += 'Upgrade-Insecure-Requests: 1\r\n'
request_string += 'Cookie: _xsrf=2|fab4a780|f1b7a8abb150de48ee31253159a0effe|1548039281\r\n'
request_string += 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.2 Safari/605.1.15\r\n'
request_string += 'Accept-Language: zh-cn\r\n'
# request_string += 'Accept-Encoding: Identify\r\n'
request_string += 'Connection: keep-alive\r\n'
request_string += '\r\n'
request_string += '\r\n'

# 发起请求
bytes_num = client_socket.send(request_string.encode('utf-8'))
print("发送数据长度：%d" % bytes_num)

# 接受服务器的响应
'''
buffers = b''
while True:
    buffer = client_socket.recv(102*10, 0)
    if not buffer:
        print('服务器发送完毕！')
        break
    buffers += buffer
    print(len(buffers))

print(buffers.decode('utf-8'))
'''

# 接受头（获取数据的长度）
header_buffer = b''
while True:
    buffer = client_socket.recv(1, 0)
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
len_content = int(len_content[0])
print(len_content)

# 接受数据体（根据长度接受）
body_buffer = b''
while True:
    buffer = client_socket.recv(10 * 1024, 0)
    body_buffer += buffer
    if len(body_buffer) == len_content:
        print('数据提读取完毕！')
        break

client_socket.close()
# print(body_buffer.decode('utf-8'))
