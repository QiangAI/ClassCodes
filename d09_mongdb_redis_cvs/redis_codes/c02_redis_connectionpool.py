# coding = utf-8
import redis.connection

pools = redis.connection.ConnectionPool(
    connection_class=redis.connection.Connection,
    max_connections=10,
    host='127.0.0.1',
    port=6379,
    db=0,
    password='yq123456')
redis = redis.client.Redis(connection_pool=pools)
print(redis.keys(pattern='*'))
