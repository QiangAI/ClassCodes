import lxml.etree

parser = lxml.etree.XMLParser()

doc = lxml.etree.parse('books.xml', parser)

root = doc.getroot()

node = root.xpath('book/title')
print(type(node), node)

print(node[0].tag)
print(node[0].text)
print(node[0].getparent().attrib)

re = root.itertext('book', 'title')
print(list(re))
print(root.tag)

nodes = root.xpath('book')

re = nodes[0].itersiblings(preceding=False)
print(type(re), list(re))
