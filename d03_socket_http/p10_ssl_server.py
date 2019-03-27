import socket
import ssl

# 构造一个ssl上下文环境
ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
# 加载服务整数与私钥

ctx.load_cert_chain(
    certfile='certs/server.crt',
    keyfile='certs/server_rsa_private',
    password='server')

# 创建socket
sk = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
    socket.IPPROTO_TCP)
# 包装socket
w_sk = ctx.wrap_socket(
    sock=sk,
    server_side=True)

# 开始通信
w_sk.bind(('', 33333))  # ssl标准端口是443
w_sk.listen(2)
print('等待客户链接')
client, (ip, port) = w_sk.accept()
print('链接：', ip, port)
# 利用包装socket进行数据交换
while True:
    buf = client.recv(4 * 1024, 0)
    if not buf:
        break
    print(buf.decode('utf-8'))
