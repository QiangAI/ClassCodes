# encoding = utf-8
import hmac
import time
from hashlib import sha1

import execjs


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


def get_encrypt(username, password, timestamp, signature):
    str_login = ""
    str_login += "client_id=c3cef7c66a1843f8b3a9e6a1e3160e20&"
    str_login += "grant_type=password&"
    str_login += "timestamp={}&"
    str_login += "source=com.zhihu.web"
    str_login += F"&signature={signature}&"
    str_login += F"username={username}&"
    str_login += F"password={password}&"
    str_login += "captcha=&"
    str_login += "lang=en&"
    str_login += "ref_source=homepage&"
    str_login += "utm_source="

    with open('p05_custom_atob.js', 'r') as fd:
        js_zhihu = fd.read()

    ctx = execjs.compile(js_zhihu)
    encrypt_ = ctx.call('Q', str_login)
    return encrypt_


timestamp = str(int(time.time() * 1000))
username = "+8613338629985"
password = "Louis123@yq"
signature = get_signature(timestamp)

encrypt = get_encrypt(username, password, timestamp, signature)
print(encrypt)
