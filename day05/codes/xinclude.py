import xml.etree.ElementInclude

xml.etree.ElementInclude.XINCLUDE_INCLUDE = '{http://www.w3.org/2003/XInclude}include'
# 非xml解析，直接返回字符串
result = xml.etree.ElementInclude.default_loader(
    href='webpages.xml',
    parse='text',
    encoding='utf-8')
print(':', type(result))
print(result)

# 作为xml解析返回xml.etree.ElementTree.Element对象。
result = xml.etree.ElementInclude.default_loader(
    href='webpages.xml',
    parse='xml',
    encoding='utf-8')

print(':', type(result))
for ele in result:
    print(type(ele), ele)
xml.etree.ElementInclude.include(result, loader=None)
for ele in result:
    print(type(ele), ele)
print(xml.etree.ElementInclude.XINCLUDE_INCLUDE)
