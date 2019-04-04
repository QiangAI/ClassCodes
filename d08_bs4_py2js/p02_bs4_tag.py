import bs4
import requests

# 下载数据
response = requests.get(url='https://ke.qq.com/course/list/python')
str_content = response.content.decode('utf-8')
# 解析 - 遍历
# 1. 加载数据
# doc = bs4.BeautifulSoup(markup=str_content, features='html5lib')
doc = bs4.BeautifulSoup(markup=str_content, features='html.parser')

for sec in doc.children:
    print(len(sec))
