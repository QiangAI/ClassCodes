# coding = utf-8
from xml.etree.ElementTree import TreeBuilder
from xml.etree.ElementTree import XMLParser


class MyBuilder(TreeBuilder):
    is_root = True
    root_element = None

    def __init__(self, element_factory=None):
        super().__init__(element_factory)

    def start(self, tag, attrs):
        elem = super().start(tag, attrs)
        if self.is_root:
            self.root_element = elem
            self.is_root = False
        return elem


builder = MyBuilder(element_factory=None)
parser = XMLParser(target=builder)
fd = open('books.xml', 'r')
xml_data = fd.read()
parser.feed(xml_data)

root = builder.root_element
for item in root.getchildren():
    print(item.tag, ':', item.attrib)
    for it in item.getchildren():
        print('\t|-', it, ':', it.tag, ':', it.text)
