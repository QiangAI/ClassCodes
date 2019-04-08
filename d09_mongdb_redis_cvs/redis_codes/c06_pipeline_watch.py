# coding = utf-8

import time

import redis.connection

pool = redis.connection.ConnectionPool(max_connections=10, host='127.0.0.1', port=6379, db=0, password='yq123456')
pipe = redis.client.Pipeline(
    connection_pool=pool,
    transaction=True,
    shard_hint=None,
    response_callbacks=[]
)
try:
    pipe.watch('py_user', )
    pipe.multi()
    pipe.set(name='py_user', value='Jack')
    time.sleep(20)
    pipe.set(name='linux_user', value='root')
    pipe.execute()
except redis.WatchError as e:
    print(e)
    # 异常抛出的时候，事务被自动取消
    pipe.reset()
