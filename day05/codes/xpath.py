import xml.etree.ElementInclude
import xml.etree.ElementPath

print(xml.etree.ElementPath.ops)
print(xml.etree.ElementPath.xpath_tokenizer_re)

root = xml.etree.ElementInclude.default_loader('books.xml', 'xml')
eles = xml.etree.ElementPath.findall(root, 'book')
print(eles)

ele = xml.etree.ElementPath.find(root, 'book')
if ele:
    print(ele.attrib)

root = xml.etree.ElementInclude.default_loader('note.xml', 'xml')
ele = xml.etree.ElementPath.findtext(root, 'to', '缺省值')
print(ele)

root = xml.etree.ElementInclude.default_loader('books.xml', 'xml')
eles = xml.etree.ElementPath.iterfind(root, 'book')
print(eles)
print(type(eles))
for e in eles:
    print(e)
