import socket

ip_addr = ('', 33333)

# 插座
sk = socket.socket(
    socket.AF_INET,  # IP格式（地址族）
    socket.SOCK_STREAM,  # 数据格式（字节流，数据报文，RAW原生数据内核数据格式：报文）
    socket.IPPROTO_TCP)  # 数据内容（协议）

# 插在网卡
sk.bind(ip_addr)
# 监听

sk.listen(2)
# sock = ssl.wrap_socket(sk)


# 接收

client_sk, (ip, port) = sk.accept()
print(ip, port)

while True:
    buf = client_sk.recv(4 * 1024, 0)
    if not buf:
        print('客户退出')
        break
    print(buf.decode('utf-8'))
    # print(buf)
