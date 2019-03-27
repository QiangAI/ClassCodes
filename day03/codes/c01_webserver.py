# coding =utf-8
import os
import select  # 多路复用模块
import signal
import socket  # socket编程模块
import sys  # 系统调用

# 方便发送信号灭掉这个进程
print('本进程ID：%d，可以使用kill灭之，如果在ipython中不方便结束的话！' % os.getpid())


# 这里处理ctrl+c的信号（方便ctrl+c退出）
def handle_int(signum, handler):
    print('程序中断退出，信号：%d' % signum, '处理器是：{}'.format(handler))
    sys.exit(0)


# 绑定对ctrl+c信号的处理
signal.signal(signalnum=signal.SIGINT, handler=handle_int)

# 下面代码为了清晰思路，没有做任何代码的异常处理
# 多路复用数据
io_inputs = []
io_outputs = []
io_error = []
# 创建socket
server_socket = socket.socket(
    socket.AF_INET,  # 网络地址族：常用的是internet网地址格式（IP地址）
    socket.SOCK_STREAM,  # 网络通信方式：流与报文两种
    socket.IPPROTO_TCP)  # 通信协议：数据包的格式

# 绑定地址
server_address = ('', 9999)  # 地址包含IP地址与端口地址
server_socket.bind(server_address)
# 监听
server_socket.listen(2)

# 把server_socket加入多路复用IO中
io_inputs.append(server_socket)

# 开始监控多路复用异步IO（包含server_socket的连接，新连接的也加入，短线的删除）
while True:
    ready_inputs, ready_outputs, ready_error = select.select(
        io_inputs, io_outputs, io_error, None)
    # 检查返回值，并相应的处理,这里我们只接收，不发送，所以不处理输出IO
    for fd in ready_inputs:
        # 服务器IO与每个客户的IO分开处理
        if fd == server_socket:  # 服务器IO
            # 对服务器IO的护处理：接收客户连接
            client_socket, client_address = fd.accept()  # 这里需要处理异常，就是服务器挂掉，退出应用
            print('客户连接：IP=%s,PORT=%d' % client_address)  # 这里需要一个元组，直接使用
            # 把新连接的客户加入多路复用监控处理
            io_inputs.append(client_socket)
        else:  # 每个客户的IO
            # 对客户IO是接收数据请求：请求都是HTTP协议的请求协议
            while True:
                buffer = fd.recv(1024 * 4, 0)  # 接收缓冲大小与接收标记
                if not buffer:
                    fd.close()  # 关闭
                    io_inputs.remove(fd)  # 客户退出
                    print('客户连退出')
                    break
                else:
                    print(buffer.decode('UTF-8'))
