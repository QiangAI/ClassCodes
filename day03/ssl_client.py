import socket
import ssl


class client_ssl:
    def send_hello(self, ):
        # 生成SSL上下文
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        # 加载信任根证书
        context.load_verify_locations('ca.crt')

        # 与服务端建立socket连接
        with socket.create_connection(('127.0.0.1', 9443)) as sock:
            # 将socket打包成SSL socket
            # 一定要注意的是这里的server_hostname不是指服务端IP，而是指服务端证书中设置的CN，我这里正好设置成127.0.1而已
            with context.wrap_socket(sock, server_hostname='SERVER') as ssock:
                # 向服务端发送信息
                msg = "do i connect with server ?".encode("utf-8")
                ssock.send(msg)
                # 接收服务端返回的信息
                msg = ssock.recv(1024).decode("utf-8")
                print(f"receive msg from server : {msg}")
                ssock.close()


if __name__ == "__main__":
    client = client_ssl()
    client.send_hello()
