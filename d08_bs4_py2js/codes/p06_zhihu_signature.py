# encoding = utf-8
import hmac
import time
from hashlib import sha1


def get_signature(now_):
    # 签名由clientId,grantType,source,timestamp四个参数生成
    h = hmac.new(
        key='d1b964811afb40118a12068ff74a12f4'.encode('utf-8'),
        digestmod=sha1)
    grant_type = 'password'
    client_id = 'c3cef7c66a1843f8b3a9e6a1e3160e20'
    source = 'com.zhihu.web'
    now = now_
    h.update((grant_type + client_id + source + now).encode('utf-8'))
    return h.hexdigest()


timestamp = str(int(time.time() * 1000))
signature = get_signature(timestamp)
print(signature)
