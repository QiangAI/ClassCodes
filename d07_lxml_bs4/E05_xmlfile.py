import lxml.etree

with lxml.etree.xmlfile("exam.xml", encoding='utf-8') as xf:
    print(dir(xf))  # 动态添加的
    xf.write_declaration(standalone=True)
    xf.write_doctype('<!DOCTYPE root SYSTEM "some.dtd">')

    with xf.element('books'):
        ele_book = lxml.etree.Element('book', {'no': '0001', 'name': '好书'})
        ele_title = lxml.etree.Element('title')
        ele_title.text = '好书'
        ele_book.append(ele_title)
        xf.write(ele_book)

    xf.flush()
