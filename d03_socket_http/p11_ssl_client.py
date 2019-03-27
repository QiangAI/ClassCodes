import socket
import ssl

# ssl上下文
ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)

# 加载证书
ctx.load_verify_locations('certs/ca.crt')
# 创建socket
sk = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
    socket.IPPROTO_TCP)
# 包装socket
w_sk = ctx.wrap_socket(
    sock=sk, server_side=False,
    server_hostname='SERVER')  # 服务器名字，来自创建服务器证书中的CN字段
# 链接
w_sk.connect(('127.0.0.1', 22222))
# 发送数据
w_sk.send('你好'.encode('utf-8'), 0)
