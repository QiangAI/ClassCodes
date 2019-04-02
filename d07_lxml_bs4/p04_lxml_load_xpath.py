import lxml.etree
import requests

# ------------------数据下载
# 1. 产生用户请求
usr_request = requests.Request(
    url='https://ke.qq.com/course/list/Python',
    method='GET',
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:66.0) Gecko/20100101 Firefox/66.0'
    },
    params={
        'price_min': '1',
        'page': 2
    }
)
# 2. 产生可以发送的请求
pre_request = usr_request.prepare()
# 3. 发送请求
session = requests.Session()
response = session.send(pre_request)

# 4. 得到需要的数据
content = response.content.decode('utf-8')
# print(content)

# ------------------数据解析

# 1. 加载数据，产生节点：节点树 <-> 节点
# parser = lxml.etree.HTMLParser()
# text = html或者xml数据，parser = 指定的解析器，base_url = ''指定html中存在相对资源，默认使用这个作为参考路径
# doc = lxml.etree.fromstring(content, parser=parser)
doc = lxml.etree.HTML(content)
# 2. 对接点树与节点，进行解析
# 第一种遍历方法
# length = len(doc)
# for idx in range(length):
#     print(doc[idx])

# # 第二种遍历方法
# for e in doc:
#     print(e)
# it = iter(doc)
# print(type(it))

# 节点元素；节点管理：获取，遍历，查找，修改，删除，

# # 第三种遍历方式（节点管理操作）
# nodes = doc.getchildren()
# for node_ in nodes:
#     print(node_)

# 把节点变换为树
# tree = doc.getroottree()
# print(type(tree))

# 节点的相关的数据：属性attrib，节点名tag，节点文本:text tail
# for e in doc:
#     print(e.attrib, e.tag, e.text)

# 属性提供给几个特殊函数get()某个属性值，items()，keys()，values
#
# for e in doc:
#     print(e.items(), e.keys(),e.values(), e.get('no','缺省值'))

# 1. find
# 节点：在子节点查找
# nodes = doc.findall('span')
# print(nodes)
# 节点的根：树才有根，才能使用/， /路径分隔符号，子节点（下一级节点）
# 。标签当前节点
# //后代节点
# nodes = doc.findall('body/.//div')
# print(len(nodes))
# tree = doc.getroottree()
# nodes = tree.findall('//div')
# print(len(nodes))
# .. 表示上一级节点
# nodes = doc.findall('body/..')
# print(len(nodes),nodes[0])
# tree = doc.getroottree()
# nodes = tree.findall('/body/..')
# print(len(nodes),nodes[0])

# find不是严格的xpath,@语法在find不处理。
# 取属性
# nodes = doc.xpath('body/header/@id')
# print(len(nodes),nodes[0])
# tree = doc.getroottree()
# nodes = tree.xpath('/html/body/header/@id')
# print(len(nodes),nodes[0])
# 取文本节点
# nodes = doc.xpath('body/header/div/div/div/a/text()')
# print(len(nodes), nodes[0])
# tree = doc.getroottree()
# nodes = tree.xpath('/html/body/header/div/div/div/a/text()')
# print(len(nodes),nodes)
# 按照位置取节点(第一个位置是1，最后一个位置last())
# nodes = doc.xpath('body/header/div/div/div/a/text()')
# print(len(nodes), nodes[0])
# tree = doc.getroottree()
# nodes = tree.xpath('/html/body/header/div/div[last()-1]')
# print(nodes)

# 使用positon()获取位置，并且做测试
# tree = doc.getroottree()
# nodes = tree.xpath('/html/body/header/div/div[position()>2]')
# print(len(nodes),nodes)
# 属性测试
# tree = doc.getroottree()
# # nodes = tree.xpath('/html/body/header/div/div[@class]/@class')
# nodes = tree.xpath('/html/body/header/div/div[@class="header-index-text"]')
# print(len(nodes),nodes)

# 访问技巧(节点做测试 node() span ='￥7280.00')
# tree = doc.getroottree()
# nodes = tree.xpath('//div[@data-report-module="middle-course"]/ul[@class="course-card-list"]/li/div[@class="item-line item-line--bottom"]/span[@class="line-cell item-price"]/text()')
# nodes = tree.xpath('//span/a/text()')
# nodes = tree.xpath('//div[@data-report-module="middle-course"]/ul[@class="course-card-list"]/li/div[span="¥7280.00"]/span/text()')
# nodes = tree.xpath('//div[@data-report-module="middle-course"]/ul[@class="course-card-list"]/li/div/span[text()="¥7280.00"]/@*')
# nodes = tree.xpath('//div[@data-report-module="middle-course"]/ul[@class="course-card-list"]/li/div[node()="¥7280.00"]/span/text()')
# print(len(nodes), nodes)

# 测试做逻辑运算 + - * div  mod 关系， 逻辑， and or
# tree = doc.getroottree()
# nodes = tree.xpath('//div[@data-report-module="middle-course"]/ul[@class="course-card-list"]/li/div[node()="¥7280.00" and not(@class="item-line item-line--bottom")]/span/text()')
# print(len(nodes), nodes)
# 多个节点合并
# tree = doc.getroottree()
# # nodes = tree.xpath('//div/span/a/@title | //h4/a/text()')
# # print(len(nodes), nodes)

# xpath轴
# tree = doc.getroottree()
# nodes = tree.xpath('//div[@data-report-module="middle-course"]/ul[@class="course-card-list"]/li/div/span/a[text()="马哥教育"]/parent::*/parent::*/parent::*/h4/a/@title')
# print(len(nodes), nodes)

# # 节点的类型测试
# tree = doc.getroottree()
# nodes = tree.xpath('/html/body//div[comment()]')
#
# print(len(nodes), nodes)

# xpath函数
tree = doc.getroottree()
nodes = tree.xpath(
    '//div[@data-report-module="middle-course"]/ul[@class="course-card-list"]/li/div/span/a[substring(text(),1,2)="马哥"]')
nodes = tree.xpath(
    '//div[@data-report-module="middle-course"]/ul[@class="course-card-list"]/li/div/span/a[starts-with(text(),"马哥")]')

print(len(nodes), nodes)

# 2. xpath

# 2. xpath

# 3. css selector
