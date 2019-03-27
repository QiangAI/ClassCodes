# coding=utf-8
import socket
import time

dest_addr = ('', 22222)
# 1.创建socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
# 2.发送到目的地
for i in range(100):
    sock.sendto(('Hello:%d' % i).encode(), dest_addr)
    time.sleep(1)
sock.close()
