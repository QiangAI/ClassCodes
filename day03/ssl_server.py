import socket
import ssl


class server_ssl:
    def build_listen(self):
        # 生成SSL上下文
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        # 加载服务器所用证书和私钥
        context.load_cert_chain('server.crt', 'server_rsa_private.pem')

        # 监听端口
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
            sock.bind(('127.0.0.1', 9443))
            sock.listen(5)
            # 将socket打包成SSL socket
            with context.wrap_socket(sock, server_side=True) as ssock:
                while True:
                    # 接收客户端连接
                    client_socket, addr = ssock.accept()
                    # 接收客户端信息
                    msg = client_socket.recv(1024).decode("utf-8")
                    print(f"receive msg from client {addr}：{msg}")
                    # 向客户端发送信息
                    msg = f"yes , you have client_socketect with server.\r\n".encode("utf-8")
                    client_socket.send(msg)
                    client_socket.close()


if __name__ == "__main__":
    server = server_ssl()
    server.build_listen()
