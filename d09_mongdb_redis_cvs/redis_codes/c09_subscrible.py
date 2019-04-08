# coding = utf-8
import redis.client

redis = redis.client.Redis(host='127.0.0.1', port=6379, db=0, password='yq123456')
sub_pub = redis.pubsub()
print(sub_pub, type(sub_pub))

sub_pub.subscribe('mychannel')
sub_pub.listen()
while True:
    result = sub_pub.parse_response()
    message = sub_pub.handle_message(result)
    print('订阅的消息：', result, message['data'])
