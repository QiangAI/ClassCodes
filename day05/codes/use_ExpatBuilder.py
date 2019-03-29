import xml.dom
import xml.dom.expatbuilder
import xml.dom.minidom

builder = xml.dom.expatbuilder.ExpatBuilder()
dom = builder.parseFile(open('note.xml', 'r'))
children = dom.childNodes
print(children)
print(dom.documentElement)


def list_nodes(nd):
    if nd.nodeType == xml.dom.Node.ELEMENT_NODE:
        print("标签名：", nd.tagName)
        # print('节点名：', nd.nodeName)
        for attr_ in nd.attributes.items():
            print(attr_.name, attr_.value)

    if nd.nodeType == xml.dom.Node.TEXT_NODE:
        print('文本：', nd.wholeText)

    if nd.nodeType == xml.dom.Node.ELEMENT_NODE and nd.hasChildNodes():
        for nd_ in nd.childNodes:
            list_nodes(nd_)


list_nodes(dom.documentElement)
