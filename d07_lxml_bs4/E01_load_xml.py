import lxml.etree

parser = lxml.etree.XMLParser()

doc = lxml.etree.parse('books.xml', parser)
print(type(doc))

fd = open('books.xml', 'br')
xml_buffer = fd.read()
fd.close()

doc = lxml.etree.fromstring(xml_buffer)
print(type(doc))

fd = open('books.xml', 'br')
xml_buffer = fd.read()
print(xml_buffer)
fd.close()

doc = lxml.etree.XML(xml_buffer)
print(type(doc))

# 下面unicode编码就不需要指定unicode
str_xml = '''<?xml version='1.0'?>
<books id="0001" name="马哥书库">
    <!--注释-->
    <book name=""><title>Python编程</title><author>赵德柱</author><year>2016</year><price>88.50</price><publisher>清华出版社</publisher></book>
    <book>
        <title>爬虫编程</title>
        <author>黄金花</author>
        <year>2018</year>
        <price>100.00</price>
        <publisher>水电出版社</publisher>
    </book>
</books>
'''

doc = lxml.etree.XML(str_xml)
print(type(doc))

str_html = '''
<!doctype html>
<html>
    <head>
        <title>标题</title>
    </head>
    <body>正文</body>
</html>

'''

doc = lxml.etree.HTML(str_html)
print(type(doc))
