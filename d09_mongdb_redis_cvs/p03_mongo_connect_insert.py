import pymongo

client = pymongo.MongoClient(host='172.16.0.200', port=9988)
# client = pymongo.MongoClient('mongodb://mage:12345678@172.16.0.200:9988/')
print(client)

# 数据库(不推荐使用：后继版本可能取消这个函数功能)
# dbs = client.database_names()
# print(dbs)

# db = client.get_database(name='lagou')
# print(type(db))

# 得到数据库
db = client.lagou
print(db)

# 得到集合
# jobs = db.get_collection('jobs')
jobs = db.jobs
print(type(jobs))

# 插入记录
# {'工作年限','学历','职位','职位ID','薪水','城市','发布时间'}
data = {
    '工作年限': '5-7年',
    '学历': '专本科',
    '职位': 'Python架构师',
    '职位ID': '000003',
    '薪水': '40k-60k',
    '城市': '上海',
    '发布时间': '2019年04月08日'
}
re = jobs.insert_one(data)
print(re, type(re))

# dbs = client.list_database_names()
#
# print(dbs)
