# coding=utf-8

import pymongo

# 创建链接
# client = pymongo.MongoClient('mongodb://Louis:12345678@127.0.0.1:9888/')

client = pymongo.MongoClient('127.0.0.1', 9888)
db = client.mege;  # 数据库

re = db.megecoll.drop()
print(re)
# 删除文档
# re = db.megecoll.remove({})
# print(type(re))
