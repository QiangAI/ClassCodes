# coding = utf-8

import redis.connection

pool = redis.connection.ConnectionPool(max_connections=10, host='127.0.0.1', port=6379, db=0, password='yq123456')
pipe = redis.client.Pipeline(
    connection_pool=pool,
    transaction=True,
    shard_hint=None,
    response_callbacks=[]
)
pipe.multi()
pipe.set(name='py_user', value='Jack')
pipe.set(name='linux_user', value='root')
# pipe.execute()
pipe.reset()  # 取消事务
