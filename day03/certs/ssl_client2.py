# coding = utf-8
import socket
import ssl

# 3.创建一个客户端socket
client_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
    socket.IPPROTO_TCP)

# 4.创建socket包装器，实现SSL通信
ssl_client_socket = ssl.wrap_socket(
    sock=client_socket,
    server_side=False,
    server_hostname='SERVER')  # 这个值是识别创建服务器证书的产品名，就是CN指定的名字

# 5.通用的socket通信模式
# 连接到服务器
ssl_client_socket.connect(('127.0.0.1', 8443))
# 发送数据
ssl_client_socket.send('来自客户的数据！'.encode('utf-8'))
# 接受数据
info = ssl_client_socket.recv(1024).decode("utf-8")
print(f"从服务器接受的信息：{info}")
ssl_client_socket.close()
