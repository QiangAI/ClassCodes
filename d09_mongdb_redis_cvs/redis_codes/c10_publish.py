# coding = utf-8
import redis.client

redis = redis.client.Redis(host='127.0.0.1', port=6379, db=0, password='yq123456')
redis.publish('mychannel', 'this is a test message')
