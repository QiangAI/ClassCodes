from xml.etree.ElementTree import ElementTree

tree = ElementTree(file='books.xml')
# e = tree.findall('book')
# print(e)
# e = tree.find('book')    # 当前节点的子节点中搜索
# print(e.tag, e.attrib, e.text)
#
# e = tree.findtext('book/title')  # 根节点，节点路径分隔符
# print(e)

# e = tree.findall('book/price')
# for e_ in e:
#     print(e_.tag, e_.text)

# e = tree.findall('book//title')  # 所有的子节点与孙子节点
# for e_ in e:
#     print(e_.tag, e_.text)

# e = tree.findall('book/./title') # 当前节点
# for e_ in e:
#     print(e_.tag, e_.text)
#
# e = tree.findall('book/title/..')   # 父节点
# for e_ in e:
#     print(e_.tag, e_.text)

# XPATH + XQuery + XLink -> XSTL(dom + css分离的原始结束)
e = tree.findall('book[@no]')
for e_ in e:
    print(e_.tag, e_.text)
