import xml.dom.domreg

# 数据
print(xml.dom.domreg.well_known_implementations)
print(xml.dom.domreg.registered)
mini_dom = xml.dom.domreg.getDOMImplementation(name='minidom')
# '4DOM'没有提供实现，下面代码会产生异常。
# four_dom = xml.dom.domreg.getDOMImplementation(name='4DOM')
print(mini_dom)
# print(four_dom)
