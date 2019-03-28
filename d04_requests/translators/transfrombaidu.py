import json
import re
import socket
import ssl

from PyQt5.QtCore import QObject

"""
专门负责爬取数据
"""


class BaiDuTranslator(QObject):

    def __init__(self):
        super().__init__()
        # 请求头
        self.request = 'POST /sug HTTP/1.1\r\n'
        self.request += 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8\r\n'
        self.request += 'Host: fanyi.baidu.com\r\n'
        self.request += 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36\r\n'
        self.request += 'Content-Length: {length}\r\n'
        self.request += 'Connection: Close\r\n'
        self.request += '\r\n'
        self.request += 'kw={keyword}'

    def translate(self, kw):
        print('开始翻译', kw)
        # 创建socket
        sk_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        # 包装socket
        ssl_sk_ = ssl.wrap_socket(sk_)
        # 链接
        ssl_sk_.connect(('fanyi.baidu.com', 443))
        # 发送请求
        l = kw.encode('utf-8')
        str_request_ = self.request.format(length=len(l) + 3, keyword=kw)
        ssl_sk_.send(str_request_.encode('utf-8'), 0)
        # 读取头
        buf_header_ = self.__read_headers(ssl_sk_)
        str_header_ = buf_header_.decode('utf-8')
        # 判定分块还是非分块
        # 读取块
        regexp = r'Content-Length: (\d*)\r\n'
        re_ = re.findall(regexp, str_header_, re.M)
        buf_body = b''
        if re_:
            print('非分包')
            len_body_ = int(re_[0], 10)
            buf_body += self.__read_block(ssl_sk_, len_body_)
            print('读取完毕')
        else:
            len_block_ = -1
            while len_block_ != 0:
                line_ = self.__read_line(ssl_sk_)
                len_block_ = int(line_[:-2].decode('utf-8'), 16)
                buf_body += self.__read_block(ssl_sk_, len_block_)
                self.__read_block(ssl_sk_, 2)
            print('读取完毕')
        ssl_sk_.close()
        sk_.close()
        # 解析数据
        json_content_ = json.loads(buf_body)
        print(json_content_)
        if json_content_['errno'] == 0:
            print(json_content_['data'][0]['v'])
            return json_content_['data'][0]['v']
        else:
            return '翻译错误'

    def __read_headers(self, s):
        buf_header = b''
        while True:
            buf = s.recv(1, 0)
            buf_header += buf
            # 取最后四个字节
            last_four_byte = buf_header[-4:]
            if last_four_byte == b'\r\n\r\n':
                print('响应头读取完毕')
                break
        return buf_header

    def __read_line(self, s):
        buffer = b''
        while True:
            buf = s.recv(1, 0)
            buffer += buf
            last_two_bytes = buffer[-2:]
            if last_two_bytes == b'\r\n':
                break
        return buffer

    def __read_block(self, s, size):
        buffer = b''
        size_ = size
        while size_ != 0:
            buf = s.recv(size_, 0)
            buffer += buf
            # 计算剩余的字节
            size_ -= len(buf)

        return buffer