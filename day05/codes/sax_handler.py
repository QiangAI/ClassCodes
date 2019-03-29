# coding = utf-8
import xml.sax.expatreader


class MyHandler(xml.sax.handler.ContentHandler):
    '''
    def setDocumentLocator(self, locator):
        print(f'system ID：{locator.getSystemId()}')
        print(f'public ID：{locator.getPublicId()}')
        print('行列位置(%d,%d)' % (locator.getLineNumber(),locator.getColumnNumber()))


    def startDocument(self):
        print('开始文档解析')

    def endDocument(self):
        print('文档解析结束')


    def startElement(self, name, attrs):
        print('元素解析开始，元素名：', name)
        # attrs是属性列表
        print(type(attrs), type(name))
        # 属性列表
        print('属性数：%d' % attrs.getLength())
        for item in attrs.items():
            print('属性名：%s，属性值：%s' % item)


    def endElement(self, name):
        print('元素解析结束，元素名：', name)

    def characters(self, content):
        # 为了看见所有的字符，下面输出采用子节序列。
        # 下面的文本包含所有元素结束的换行字符。
        print(content.encode('utf-8'))

    def startElementNS(self, name, qname, attrs):
        print(name, qname)

    def endElementNS(self, name, qname):
        print('结束：', name, qname)


    def startPrefixMapping(self, prefix, uri):
        print(prefix, uri)

    def endPrefixMapping(self, prefix):
        print(prefix)
    '''

    def processingInstruction(self, target, data):
        print('processingInstruction', target, data)


handler = MyHandler()
error = xml.sax.ErrorHandler()

# namespaceHandling 对具有命名空间的元素处理，没有命名空间设置围为0。
parser = xml.sax.expatreader.ExpatParser(namespaceHandling=0)
parser.setContentHandler(handler)
parser.setErrorHandler(error)
parser.setDTDHandler(handler)
parser.parse('note.xml')
