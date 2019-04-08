# coding = utf-8

import redis.connection


# 返回每个命名执行的结果
def my_call(*p):
    print(*p)


pool = redis.connection.ConnectionPool(max_connections=10, host='127.0.0.1', port=6379, db=0, password='yq123456')
pipe = redis.client.Pipeline(
    connection_pool=pool,
    transaction=True,
    shard_hint=None,
    response_callbacks={'SET': my_call}
)
pipe.multi()
pipe.set(name='py_user', value='Jack')
pipe.set(name='linux_user', value='root')
pipe.execute()
