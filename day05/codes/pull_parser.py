# coding = utf-8
from xml.etree.ElementTree import XMLPullParser

events = ("start", "end", "start-ns", "end-ns")
parser = XMLPullParser(events=events)
fd = open('books.xml', 'r')
xml_data = fd.read()
parser.feed(xml_data)
# 转换成列表操作
re_events = list(parser.read_events())
# 构造xml的root
root_element = re_events[0][1]


# 从根节点偏离element树
def list_tree(element, depth):
    print('\t' * depth, element.tag, ":", element.text if element.text.strip() != '' else '')
    children_elements = element.getchildren()
    if children_elements:
        for e_ in children_elements:
            list_tree(e_, depth + 1)


list_tree(root_element, 0)
