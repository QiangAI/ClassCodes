import xml.dom.xmlbuilder

builder = xml.dom.xmlbuilder.DOMBuilder()

input_stream = xml.dom.xmlbuilder.DOMInputSource()
# input_stream.encoding = 'utf-8'
# input_stream.systemId = 'http://mybatis.org/dtd/mybatis-3-config.dtd'
# input_stream.publicId = '-//mybatis.org//DTD Config 3.0//EN'
input_stream.byteStream = open('books.xml', 'r')

result = builder.parse(input_stream)
print(result)
print(result.documentElement.nodeName)
