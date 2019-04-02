import lxml.etree

parser = lxml.etree.XMLParser()

doc = lxml.etree.parse('books.xml', parser)

# node = doc.find('book[@no="0002"]/title')
# node = doc.findall('book[@no="0002"]/title')
# node = doc.findtext('book[@no="0002"]/title')

node = doc.xpath('book[@no="0002"]/title/text()')
print(type(node), node)
node = doc.xpath('book/@no')
print(type(node), node)
