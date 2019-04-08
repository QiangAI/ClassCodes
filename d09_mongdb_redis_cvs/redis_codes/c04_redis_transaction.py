# coding = utf-8

import redis.client

redis = redis.client.Redis(host='127.0.0.1', port=6379, db=0, password='yq123456')
pipeline = redis.pipeline(transaction=True)  # 参数指定是否每个指令后自动提交事务。
pipeline.multi()
pipeline.set(name='py_user', value='Jack')
pipeline.execute()
