# coding = utf-8
import xml.sax.expatreader


class MyHandler(xml.sax.handler.ContentHandler, xml.sax.handler.DTDHandler):
    def setDocumentLocator(self, locator):
        print('setDocumentLocator')

    def startDocument(self):
        print('startDocument')

    def endDocument(self):
        print('endDocument')

    def startPrefixMapping(self, prefix, uri):
        print('startPrefixMapping')

    def endPrefixMapping(self, prefix):
        print('endPrefixMapping')

    def startElement(self, name, attrs):
        print('startElement')

    def endElement(self, name):
        print('endElement')

    def startElementNS(self, name, qname, attrs):
        print('startElementNS')

    def endElementNS(self, name, qname):
        print('endElementNS')

    def characters(self, content):
        print('characters')

    def ignorableWhitespace(self, whitespace):
        print('ignorableWhitespace')

    def processingInstruction(self, target, data):
        print('processingInstruction')

    def skippedEntity(self, name):
        print('skippedEntity')

    def notationDecl(self, name, publicId, systemId):
        print('notationDecl')

    def unparsedEntityDecl(self, name, publicId, systemId, ndata):
        print('unparsedEntityDecl')


class MyError(xml.sax.ErrorHandler):

    def error(self, exception):
        print('error')
        return super().error(exception)

    def fatalError(self, exception):
        print('fatalError')
        return super().fatalError(exception)

    def warning(self, exception):
        print('warning')
        super().warning(exception)


'''
xml.sax.parse(
    source='books.xml',
    handler=MyHandler(),
    errorHandler=MyError())
'''
handler = MyHandler()
error = MyError()
# parser = xml.sax.make_parser()
parser = xml.sax.expatreader.ExpatParser(namespaceHandling=True)
print(parser)
parser.setContentHandler(handler)
parser.setErrorHandler(error)
parser.setDTDHandler(handler)
parser.parse('web.xml')
