import sys

import bs4.element
import requests

url = 'https://ke.qq.com/course/list?mt=1001&st=2002&tt=3019&price_min=0&price_max=0&page=1'
session = requests.Session()
response = session.get(url)
if not response:
    sys.exit(0)

content_html = response.content.decode('utf-8')

bs_content = bs4.BeautifulSoup(content_html, "html.parser")
# list_course = bs_content.find_all(
#     name='li',
#     attrs={
#         'class': "course-card-item"
#     },
#     recursive=False,
#     text=None,
#     limit=None
# )
# print(type(list_course))
# print(len(list_course))
# list_course = bs_content.find_all(
#     name='a',
#     attrs={'class': "item-source-link"},
#     text='马哥教育'
# )
# print(len(list_course))

# print(bs_content.children)
# for item_ in bs_content.children:
#     print(type(item_))

# print(bs_content.name)
# print(bs_content.attrs)
# print(bs_content.builder)
# print(bs_content.namespace)
# print(bs_content.prefix)
# print(bs_content.parent)
# print(bs_content.previous)
# print(bs_content.is_xml)
# print(bs_content.contents)
#
#
# print(bs_content.html['lang'])
# print(bs_content.html.attrs)
# print(bs_content.html.get('lang'))

# print('节点:', bs_content.html.body.section.div.h1)
# print('string:', bs_content.html.body.section.div.h1.string)
# print('text:', bs_content.html.body.section.div.h1.text)
#
# print('节点:', bs_content.html.body.section.div.div.a)
# print('string:', bs_content.html.body.section.div.div.a.string)
# print('text:', bs_content.html.body.section.div.div.a.text)

#
# for item_ in bs_content.children:
#     if type(item_) == bs4.element.Comment:
#         print(dir(item_))
#         print(item_.name, item_.string)
#         break

# results = bs_content.find_all(
#     name=['div', 'a'],
#     attrs={'class': ['market-bd market-bd-6 course-list course-card-list-multi-wrap js-course-list',
#                      'item-source-link']}
# )
# print(len(results))

# results = bs_content.find_all(
#     name=re.compile(r'\w{3}'),
#     attrs={'class': re.compile(r'\w{10,}')}
# )
# print(len(results))


# def node_func(value):
#     # print('节点:', type(value))
#     if value.name == 'div' or value.name == 'a':
#         return True
#     else:
#         return False
#
#
# def attr_func(value):
#     # print('属性:', type(value), value)
#     if value == 'market-bd':
#         return True
#     return False
#
#
# results = bs_content.find_all(
#     name=node_func,
#     attrs={'class': attr_func}
# )
# print(len(results))
#
# results = bs_content.find_all(class_='item-source-link')
# print(len(results))
# def div_candidate_generator(tag):
#     print(tag.name)
#     print(len(list(tag.descendants)))
#     for item_ in tag.descendants:
#         if isinstance(item_, bs4.element.Tag):
#             yield item_
#
#
# result = bs_content.select(
#     selector='div > div',
#     _candidate_generator=div_candidate_generator,
#     limit=300)
# print(len(result))
# result = bs_content.select('span')
# print(len(result))

# result = bs_content.select('#js_main_nav')
# print(len(result))
# 实际的属性是多个值： main autoM clearfix
# result = bs_content.select('.main')
# print(len(result))
# result = bs_content.select('*')
# print(len(result))

# # 所有具有type属性的节点
# result = bs_content.select('[type]')
# print(len(result))
# # 选择属性type=text/javascript的节点
# result = bs_content.select('[type=text/javascript]')
# print(len(result))
# # 属性class中含有main单词的节点
# result = bs_content.select('[class~=main]')
# print(len(result))
# # 选择type属性以text开头所有节点
# result = bs_content.select('[type|=text]')
# print(len(result))

# # 选择节点section与div
# result = bs_content.select('section,div')
# print(len(result))
# # 选择节点section内的所有div节点
# result = bs_content.select('section div')
# print(len(result))
# # 选择节点section的div子节点
# result = bs_content.select('section > div')
# print(len(result))
# # 选择节点section后的div节点
# result = bs_content.select('header + section')
# print(len(result))
#
# # 所有具有type属性的script节点
# result = bs_content.select('script[type]')
# print(len(result))
# # 选择属性type=text/javascript的script节点
# result = bs_content.select('script[type=text/javascript]')
# print(len(result))
# # 属性class中含有main单词的section节点
# result = bs_content.select('section[class~=main]')
# print(len(result))
# # 选择class属性以topic开头所有section节点
# result = bs_content.select('section[class|="topic"]')
# print(len(result))

# # # 选择节点section的div子节点
# result = bs_content.select('section > div > div[class~="course-list"]')
# print(len(result))
# for item_ in result:
#     print(item_.attrs)
#
# result = bs_content.select('section > div > [class~="course-list"]')
# print(len(result))
# for item_ in result:
#     print(item_.attrs)
#
# result = bs_content.select('section > div > .market-bd-6')
# print(len(result))
# for item_ in result:
#     print(item_.attrs)
