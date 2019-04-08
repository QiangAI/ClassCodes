import codecs
import csv

# 准备好打开的文件
fd = open('tencent.csv', 'w')
# 数据格式（数据字段）
fields = ['课程名称', '机构名称', '报名人数', '课程价格', '学习方式']

writer = csv.DictWriter(f=fd, fieldnames=fields, dialect='excel')
# writer = csv.writer(fd,dialect='excel')
# 编码（BOM）
fd.write(codecs.BOM_UTF8.decode('utf-8'))  # BOM UTF-8，每个文件钱慢三个字节用来表示
# 写一个头
writer.writeheader()
# 写多个行
data = {}
data['课程名称'] = 'Python开发'
data['机构名称'] = '马哥'
data['报名人数'] = 100
data['课程价格'] = 7288.00
data['学习方式'] = '随到随学'
writer.writerow(data)

data2 = {
    '课程名称': 'K8S精通',
    '机构名称': '马哥',
    '报名人数': 88,
    '课程价格': 2000.00,
    '学习方式': '线上'
}

writer.writerow(data2)

fd.close()
