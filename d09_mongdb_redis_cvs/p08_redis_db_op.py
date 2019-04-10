import redis.connection

pools = redis.connection.ConnectionPool(
    connection_class=redis.connection.Connection,
    max_connections=10,
    host='127.0.0.1',
    port=6379,
    db=0,
    password='12345678')

# 使用Redis
client = redis.Redis(connection_pool=pools)

# 字符串操作
# client.set(name='name', value='Louis')
# client.set(name='age', value=20)
# client.save()
# pools.disconnect()
# client.shutdown()

val = client.get('age')

print(val)

# client.shutdown()

# 下课对每种数据都操作一下。
