# coding =utf-8
import urllib.parse

split_result = urllib.parse.urlsplit(
    'http://joe:joespasswd@www.joes-hardware.com:8888/sales_info.txt;hehehe=566?name=com&age=com#anchor')

# 返回元组类型：DefragResult
print(split_result)
print(type(split_result))
print(isinstance(split_result, tuple))
print(split_result[0], split_result[1])
print(split_result.geturl())
print('fragment:', split_result.fragment)
print('hostname:', split_result.hostname)
print('netloc:', split_result.netloc)
print('password:', split_result.password)
print('path:', split_result.path)
print('port:', split_result.port)
print('query:', split_result.query)
print('scheme:', split_result.scheme)
print('username:', split_result.username)
