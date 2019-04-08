import pymongo

# 链接
client = pymongo.MongoClient(host='172.16.0.200', port=9988)
# 数据库
db = client.lagou
# 数据表（集合）
col = db.jobs

result_set = col.find({'职位ID': {'$eq': '000002'}})
print(result_set)
for rec in result_set:
    print(rec)

client.close()
