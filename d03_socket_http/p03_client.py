import socket

unix_addr = 'file.socket'
ip_addr = ('', 11111)

# sk = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM, 0)

sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

sk.sendto('你好'.encode(), ip_addr)
