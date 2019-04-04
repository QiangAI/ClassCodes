import bs4
import requests

# 下载数据
response = requests.get(url='https://ke.qq.com/course/list/python')
str_content = response.content.decode('utf-8')
# 解析 - 遍历
# 1. 加载数据
# doc = bs4.BeautifulSoup(markup=str_content, features='html5lib')
doc = bs4.BeautifulSoup(markup=str_content, features='html.parser')
# 2. 传统遍历
nodes = doc.children
for node in nodes:
    # print(type(node))
    if isinstance(node, bs4.element.Doctype):
        # print(node.name, node.PREFIX, node.SUFFIX, node)
        print(node.PREFIX, node, node.SUFFIX)

    if isinstance(node, bs4.element.Comment):
        print(node.PREFIX, node, node.SUFFIX)

    if isinstance(node, bs4.element.NavigableString):
        print(node)
