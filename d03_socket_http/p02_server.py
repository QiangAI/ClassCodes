import socket

ip_addr = ('', 11111)
unix_addr = 'file.socket'

# 创建套接字socket
# sk = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM, 0)
sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
# 绑定地址
sk.bind(ip_addr)
# 监听

# 接收用户链接
# 为这个用户创建缓冲（客户代理）

# 从客户缓冲读取数据
while True:
    buf = sk.recv(1024 * 1, 0)
    if not buf:
        break
    print((buf.decode()))
