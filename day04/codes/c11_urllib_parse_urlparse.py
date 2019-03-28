# coding =utf-8
import urllib.parse

parse_result = urllib.parse.urlparse(
    'http://joe:joespasswd@www.joes-hardware.com:8888/sales_info.txt;hehehe=566?name=com&age=com#anchor')

# 返回元组类型：DefragResult
print(parse_result)
print(type(parse_result))
print(isinstance(parse_result, tuple))
print(parse_result[0], parse_result[1])
print(parse_result.geturl())
print('fragment:', parse_result.fragment)
print('hostname:', parse_result.hostname)
print('netloc:', parse_result.netloc)
print('params:', parse_result.params)
print('password:', parse_result.password)
print('path:', parse_result.path)
print('port:', parse_result.port)
print('query:', parse_result.query)
print('scheme:', parse_result.scheme)
print('username:', parse_result.username)
