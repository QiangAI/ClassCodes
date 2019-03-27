# coding =utf-8
import socket

dest_addr = ('', 22222)
# os.unlink(dest_addr)
# 1.创建socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
# 2.绑定地址
sock.bind(dest_addr)
# 3.接收数据
while True:
    buf = sock.recv(16)
    if not buf:
        break
    print(buf.decode())
sock.close()
