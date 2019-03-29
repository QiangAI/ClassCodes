# coding = utf-8
import xml.dom.minidom

implementation = xml.dom.minidom.getDOMImplementation()
print(implementation)
doc_type = implementation.createDocumentType(
    qualifiedName='HH',
    publicId='-//mybatis.org//DTD Config 3.0//EN',
    systemId='http://mybatis.org/dtd/mybatis-3-config.dtd')

# writer = implementation.createDOMWriter()   # 没有实现，直接使用文件描述符号。
doc = xml.dom.minidom.Document()
doc.documentURI = 'http://xmlns.jcp.org/xml/ns/javaee'
doc.doctype = doc_type
# 创建根节点
root_element = doc.createElement('myroot')
attr1 = doc.createAttribute('属性')
attr1.value = '属性值'
root_element.setAttributeNode(attr1)
# doc.documentElement只读，创建文档的时候唯一产生
doc.appendChild(root_element)

# 产生文本子节点
txt = doc.createTextNode('我是文本')
root_element.appendChild(txt)

with open('your.xml', 'w') as fd:
    doc.writexml(fd,
                 indent='\t',
                 addindent='\t',
                 newl='\n',
                 encoding='utf-8')
