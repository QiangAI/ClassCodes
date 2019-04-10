import redis

# 产生链接
client = redis.Redis(password='12345678')

# 发送消息
client.publish('mymsg', '我是消息')
