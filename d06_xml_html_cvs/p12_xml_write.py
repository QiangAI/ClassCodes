import xml.dom.minidom

# 创建文档
doc = xml.dom.minidom.Document()

# 创建节点（属性）：文本
root_node = doc.createElement('books')
name_attr = doc.createAttribute('name')
name_attr.value = '马帅哥'
# ....
txt_node = doc.createTextNode('数据')

# 把属性加入根节点
root_node.setAttributeNode(name_attr)
# 把文本加入节点
root_node.appendChild(txt_node)
# 把根节点，写入文档
doc.appendChild(root_node)

fd = open('mybook.xml', 'w')

doc.writexml(fd, indent='', addindent='', newl='\n')
fd.close()
