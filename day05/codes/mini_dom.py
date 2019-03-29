import xml.dom
import xml.dom.minidom
import xml.sax

dom = xml.dom.minidom.parse(
    'note.xml',
    # parser=None,    # parser = xml.sax.make_parser()或者ExpatParser对象
    parser=xml.sax.make_parser(),
    bufsize=1024 * 10)
children = dom.childNodes


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


list_nodes(children[0])
