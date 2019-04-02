import xml.etree.ElementTree

tree = xml.etree.ElementTree.ElementTree(file='books.xml')

# print(tree)
#
# tree2 = xml.etree.ElementTree.ElementTree()
# tree2.parse('books.xml')
# print(tree2)
# list的方式遍历:节点名，属性，文本，子节点
root = tree.getroot()
for ele_ in root:
    print(ele_.tag, ele_.attrib, ele_.text)
    for e_ in ele_.getchildren():
        print(e_.tag, e_.attrib, e_.text)

# 使用xpath的方式查找tree：Element支持xpath，find
# find
# findall
# findtext
