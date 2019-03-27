# coding=utf-8

import socket

sk = socket.getaddrinfo('baidu.com', 80, proto=socket.IPPROTO_TCP)
for _, _, _, _, (ip, port) in sk:
    print(ip, port)
