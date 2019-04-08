# coding=utf-8

import pymongo

# 创建链接
# client = pymongo.MongoClient('mongodb://Louis:12345678@127.0.0.1:9888/')

client = pymongo.MongoClient('127.0.0.1', 9888)
db = client.mege;  # 数据库

cur = db.megecoll.find({"course_name": "nuge"});  # 数据集（游标形式返回）

# 遍历数据集
for document in cur:
    print(document);  # 打印每条记录
