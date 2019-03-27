# coding = utf-8
import socket
import ssl

# 1. 创建SSL上下文，需要指定版本,缺省的是PROTOCOL_TLS，我们指定服务器签名PROTOCOL_TLS_SERVER
# 这一步的关键是选择合适的版本，每个不同的版本之间是不互融的。
ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)

# 2. 加载证书与服务器私钥
ctx.load_cert_chain(certfile='server.crt',  # 服务器已经签名的证书
                    keyfile='server_rsa_private.pem',  # 服务器私钥
                    password='server')  # 生成服务器时输入的密码（这里不指定，就需要输入）

# 3. 创建socket
server_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
    socket.IPPROTO_TCP)

# 4. 使用ctx创建一个包装器socket，该socket具有签名加密功能。
ssl_server_socket = ctx.wrap_socket(
    sock=server_socket,  # 被包装的socket
    server_side=True)  # 指定是服务器测签名加密

# 5. 正常的socket通信操作
# 绑定服务器地址
ssl_server_socket.bind(('', 8443))  # 443时SSL通用端口,注意使用元组表示地址格式
# 监听
ssl_server_socket.listen(2)
while True:
    # 接受客户连接
    print('等待客户连接！')
    client_socket, client_address = ssl_server_socket.accept()
    print('有客户连接：', client_address)
    # 接受客户数据
    info = client_socket.recv(1024).decode("utf-8")
    print(f"从客户{client_address}接受的信息{info}")
    # 给客户发送一个信息
    client_socket.send('来自服务器的信息！收到没有？'.encode('utf-8'))
    client_socket.close()
    break

ssl_server_socket.close()
