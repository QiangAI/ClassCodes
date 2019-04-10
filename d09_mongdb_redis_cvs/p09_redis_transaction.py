import redis.connection

# 使用Redis
client = redis.Redis(host='127.0.0.1', port=6379, db=0, password='12345678')

# 使用管道（显式事务处理）
pipeline = client.pipeline(transaction=True)
# 开始事务
pipeline.multi()
# 数据操作
client.set(name='Jack', value='20')
# 其他数据操作
# 添加，修改，删除
# 提交事务
pipeline.execute()

# 默认操作会自动产生事务提交（隐形事务）
