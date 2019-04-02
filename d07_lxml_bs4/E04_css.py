import lxml.cssselect
import lxml.etree

parser = lxml.etree.XMLParser()

doc = lxml.etree.parse('books.xml', parser)

root = doc.getroot()

selector = lxml.cssselect.CSSSelector('books > book')
print(selector.path)
re = selector(root)
print(type(re), re)

re = root.cssselect('books > book', translator='html')
print(type(re), re)
