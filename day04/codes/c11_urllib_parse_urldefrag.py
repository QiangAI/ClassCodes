# coding =utf-8
import urllib.parse

defrag = urllib.parse.urldefrag(
    'http://joe:joespasswd@www.joes-hardware.com/sales_info.txt?name=com&age=com#anchor')

# 返回元组类型：DefragResult
print(defrag)
print(type(defrag))
print(isinstance(defrag, tuple))
print(defrag[0], defrag[1])

print(defrag.geturl())  # 全部
print(defrag.url)  # 除去碎片以后的url
print(defrag.fragment)

# 返回值的计数与索引，这个例子就两个值：url与defrag
print(defrag.count('anchor'))
print(defrag.index('anchor'))