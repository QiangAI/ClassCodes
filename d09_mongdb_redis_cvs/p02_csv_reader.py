import csv

fd = open('tencent.csv', 'r')

fields = ['课程名称', '机构名称', '报名人数', '课程价格', '学习方式']
reader = csv.DictReader(f=fd, fieldnames=fields, dialect='excel')

for row in reader:
    print(row)

fd.close()

