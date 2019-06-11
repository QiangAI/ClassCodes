import redis.client


class RedisMQ(object):
    ip = '127.0.0.1'
    port = 6379
    db = 0
    key = 'category_task'
    conn = None

    def __init__(self, key_='category_task'):
        self.key = key_
        # 链接服务器（考虑异常处理）
        self.conn = redis.client.Redis(host=self.ip, port=self.port, db=self.db)

    # 链接redis数据库（需要的时候重新调用）
    def connect(self):
        try:
            self.conn = redis.client.Redis(host=self.ip, port=self.port, db=self.db)
        except Exception as e:
            raise Exception()

    # 把分类的爬取任务放入任务队列
    def push_task(self, item):
        # 这里考虑异常处理
        self.conn.rpush(self.key, item)

    # 获取任务队列
    def pop_task(self):
        # 使用阻塞队列（注意返回元组（key ，value），key是队列的key）
        return self.conn.blpop(self.key, timeout=60)  # 延时时间单位为秒

# mq = RedisMQ()
# re = mq.pop_task()
# print(re[0], re[1])
# ff = json.loads(re[1])
