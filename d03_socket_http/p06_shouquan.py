import socket

ip_addr = ('', 22222)

# 插座
sk = socket.socket(
    socket.AF_INET,  # IP格式（地址族）
    socket.SOCK_STREAM,  # 数据格式（字节流，数据报文，RAW原生数据内核数据格式：报文）
    socket.IPPROTO_TCP)  # 数据内容（协议）

# 插在网卡
sk.bind(ip_addr)
# 监听

sk.listen(2)

# 接收

client_sk, (ip, port) = sk.accept()
print(ip, port)
# str_response = 'HTTP/1.1 401 Unauthorized\r\n'
str_response = 'HTTP/1.1 300 ok\r\n'
str_response += 'Refresh:3; url=https://www.baidu.com'
# str_response += 'WWW-Authenticate: Basic realm="Louis!"\r\n'
# str_response += 'Connection: Keep-Alive\r\n'
# str_response += 'Keep-Alive: 115\r\n'
str_response += '\r\n\r\n'

client_sk.send(str_response.encode('utf-8'), 0)

while True:
    buf = client_sk.recv(1024 * 4, 0)
    if not buf:
        break
    print(buf.decode())

client_sk.close()
sk.close()
