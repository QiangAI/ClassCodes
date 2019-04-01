import xml.dom.expatbuilder

builder = xml.dom.expatbuilder.ExpatBuilder()

fd = open('books.xml')

# doc = builder.parseFile(fd)
doc = builder.parseString(fd.read())  # 封装的所有细节全部是基于SAX模型
print(doc)
fd.close()

# 解析节点
nodes = doc.childNodes
for node_ in nodes:
    nodes_1 = node_.childNodes
    for node2_ in nodes_1:
        print(node2_.nodeName)
