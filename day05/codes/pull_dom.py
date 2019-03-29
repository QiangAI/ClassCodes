import xml.dom.pulldom
import xml.sax.expatreader

# 方式一：
result = xml.dom.pulldom.parse('books.xml')
e, doc = result.getEvent()
print(e)
print(doc.documentElement)

# 方式二：
parser = xml.sax.expatreader.ExpatParser(namespaceHandling=True)
fd = open('books.xml', 'r')
ds = xml.dom.pulldom.DOMEventStream(fd, parser=parser, bufsize=1024 * 10)
e_, doc_ = ds.getEvent()
print(e_)
