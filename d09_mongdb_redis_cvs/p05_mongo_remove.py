import pymongo

# 链接
client = pymongo.MongoClient(host='172.16.0.200', port=9988)
# 数据库
db = client.lagou
# 数据表（集合）
col = db.jobs

col.remove()
# col.remove({})  # 条件

client.close()
