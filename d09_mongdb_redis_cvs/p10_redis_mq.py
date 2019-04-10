import redis

# 链接
client = redis.Redis(host='127.0.0.1', port=6379, db=0, password='12345678')
# 得到订阅对象
subpub = client.pubsub()
print(type(subpub))
# 监听
subpub.subscribe('mymsg')  # 订阅指定消息通道
subpub.listen()

# 处理消息(下面程序运行需要发送消息：redis-cli：手工发送| 程序发送)

while True:
    print('接收消息')
    result = subpub.parse_response(block=True)  # 阻塞函数
    print('解析消息')
    msg = subpub.handle_message(response=result)
    print('接收的消息是：', msg['data'])
