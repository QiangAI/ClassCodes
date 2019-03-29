# coding = utf-8
from xml.etree.ElementTree import ElementTree

tree = ElementTree()
tree.parse('books.xml')

root_element = tree.getroot()


# 从根节点偏离element树
def list_tree(element, depth):
    print('\t' * depth, element.tag, ":", element.text if element.text.strip() != '' else '')
    children_elements = element.getchildren()
    if children_elements:
        for e_ in children_elements:
            list_tree(e_, depth + 1)


list_tree(root_element, 0)
