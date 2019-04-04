import bs4
import requests

# 下载数据
response = requests.get(url='https://ke.qq.com/course/list/python')
str_content = response.content.decode('utf-8')
# 解析 - 遍历
# 1. 加载数据
# doc = bs4.BeautifulSoup(markup=str_content, features='html5lib')
doc = bs4.BeautifulSoup(markup=str_content, features='html.parser')

#
nodes = doc.find_all(
    name='div',
    # attrs={'data-report-module':'middle-course'},
    attrs={'class': "market-bd market-bd-6 course-list course-card-list-multi-wrap js-course-list"},
    recursive=True,
    text=None,
    limit=None,  # data_report_module='middle-course'
    # class_="market-bd market-bd-6 course-list course-card-list-multi-wrap js-course-list"
)
print(len(nodes))
