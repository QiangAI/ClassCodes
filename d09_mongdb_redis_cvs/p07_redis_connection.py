import redis.connection

# 获取对redis数据库服务器的链接（单链接）
# client = redis.Redis(host='127.0.0.1', port=6379, db=0, password='12345678')
# print(client)
# # 通用访问
# keys = client.keys('*')
# print(keys)

# 连接池（应用场景：多个线程同时访问Redis服务器，一般会采用连接池）
pools = redis.connection.ConnectionPool(
    connection_class=redis.connection.Connection,
    max_connections=10,
    host='127.0.0.1',
    port=6379,
    db=0,
    password='12345678')

# 使用Redis
client = redis.Redis(connection_pool=pools)
keys = client.keys('*')
print(keys)

# 1. 字符串
# 2. hash：字典
# 3. list
# 4. set
# 5. sorted_set

# 6. 事务
# 7. 消息队列
