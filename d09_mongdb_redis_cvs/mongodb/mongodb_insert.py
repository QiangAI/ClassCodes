# coding=utf-8

import pymongo

# 创建链接
# client = pymongo.MongoClient('mongodb://Louis:12345678@127.0.0.1:9888/')

client = pymongo.MongoClient('127.0.0.1', 9888)
db = client.mege;  # 数据库

data = {
    "course_name": "马哥数据分析",
    "course_price": 8888,
    "course_teacher": "Louis Young"
}
re = db.megecoll.insert_one(data)
print(type(re))
# 多条数据的插入： insert_many
