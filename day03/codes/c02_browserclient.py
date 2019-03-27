# coding = utf-8
import re
import signal
import socket
import sys


# 这里处理ctrl+c的信号（方便ctrl+c退出）
def handle_int(signum, handler):
    print('程序中断退出，信号：%d' % signum, '处理器是：{}'.format(handler))
    client_socket.close()
    sys.exit(0)


# 绑定对ctrl+c信号的处理
signal.signal(signalnum=signal.SIGINT, handler=handle_int)

server_name = 'www.huanqiu.com'
# 获取IP地址（这个过程不是必须的）
list_info = socket.getaddrinfo(
    host=server_name,
    port=80,
    family=socket.AF_INET,
    type=socket.SOCK_STREAM,
    proto=socket.IPPROTO_TCP,
    flags=socket.AI_ALL)  # socket.AI_***参数的一部分
for _, _, _, _, address in list_info:
    print('IP：%s，PORT：%d' % address)

# 创建socket
client_socket = socket.socket(
    socket.AF_INET,  # 网络地址族：常用的是internet网地址格式（IP地址）
    socket.SOCK_STREAM,  # 网络通信方式：流与报文两种
    socket.IPPROTO_TCP)  # 通信协议：数据包的格式

# 连接到到服务器（取上面取出的第一个INET地址）
print(list_info[0][-1])
client_socket.connect(list_info[0][-1])  # 没有返回值，需要进行异常处理，这里容易被信号中断

# 发送数据
request_string = ''
request_string += 'GET / HTTP/1.1\r\n'
request_string += 'Host: %s:9999\r\n' % server_name  # 可以替换成IP地址
request_string += 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n'
request_string += 'Upgrade-Insecure-Requests: 1\r\n'
request_string += 'Cookie: _xsrf=2|f877d065|146c6a9838e67ba203776913fae34f45|1547796259\r\n'
request_string += 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.2 Safari/605.1.15\r\n'
request_string += 'Accept-Language: zh-cn\r\n'
# request_string += 'Accept-Encoding: gzip, deflate\r\n'
request_string += 'Connection: keep-alive\r\n'
request_string += '\r\n'
request_string += '\r\n'

bytes_num = client_socket.send(request_string.encode('UTF-8'))
print('发送成功的字节数：%d' % bytes_num)

# 接收服务器响应的协议数据
header_buffers = b''
while True:
    # 一个子节一个子节读取
    buffer = client_socket.recv(1, 0)  # MSG_**等
    header_buffers += buffer
    # 判定最后四个子节是否是'\r\n\r\n'：表示响应头读完
    last_four_bytes = header_buffers[-4:]  # 取最后四个子节
    if last_four_bytes == b'\r\n\r\n':
        break  # header结束

# 把子节转换为字符串
header_string = header_buffers.decode('utf-8')
print('响应协议头：\n', header_string)
# 获取请求体的长度
regex = r'Content-Length: (\d*?)\r\n'
len_content = re.findall(regex, header_string, re.MULTILINE)
len_content = int(len_content[0])
print('响应正文长度为：{}'.format(len_content))

# 下面读取响应正文
body_buffers = b''
while True:
    buffer = client_socket.recv(1024 * 10, 0)  # MSG_**等
    body_buffers += buffer
    if len(body_buffers) == len_content:
        break

print('响应体读取完毕！')
body_string = body_buffers.decode('utf-8')
# print(body_string)
