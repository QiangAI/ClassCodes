# coding=utf-8
import base64
import hmac
import json
import time
from hashlib import sha1

import execjs
import requests


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


def get_encrypt(username, password, timestamp, signature, captcha):
    str_login = ""
    str_login += "client_id=c3cef7c66a1843f8b3a9e6a1e3160e20&"
    str_login += "grant_type=password&"
    str_login += F"timestamp={timestamp}&"
    str_login += "source=com.zhihu.web"
    str_login += F"&signature={signature}&"
    str_login += F"username={username}&"
    str_login += F"password={password}&"
    str_login += F"captcha={captcha}&"
    str_login += "lang=en&"
    str_login += "ref_source=homepage&"
    str_login += "utm_source="

    with open('p05_custom_atob.js', 'r') as fd:
        js_zhihu = fd.read()

    ctx = execjs.compile(js_zhihu)
    encrypt_ = ctx.call('Q', str_login)
    return encrypt_


timestamp = str(int(time.time() * 1000))
username = "13338629985"
password = "Louis123@yq"
signature = get_signature(timestamp)

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.1 Safari/605.1.15',
}
session = requests.Session()
session.headers = headers
#
url_captcha = 'https://www.zhihu.com/api/v3/oauth/captcha?lang=en'
res_captcha = session.get(url_captcha)
print(res_captcha.cookies)
is_captcha = json.loads(res_captcha.content.decode())['show_captcha']
print(is_captcha)
captcha_code = ''
if is_captcha:
    # 获取校验码
    res_captcha = session.put(url_captcha)
    if res_captcha.status_code == 202:
        base64_img = json.loads(res_captcha.content.decode())['img_base64']
        icaptcha_img = base64.b64decode(base64_img)
        with open("zhihu.png", 'wb') as fd:
            fd.write(icaptcha_img)
            print("产生校验码")
        # 校验：
        # input
        captcha_code = input("输入校验码")
        data = {
            'input_text': captcha_code
        }

        res_captcha = session.post(url_captcha, data)
        print(res_captcha.content.decode())
        if res_captcha.status_code == 201:
            captcha_ok = json.loads(res_captcha.content.decode())['success']
            print(captcha_ok)
            if captcha_ok:
                print("校验码通过")

else:
    print("不需要校验")

# 登录
encrypt = get_encrypt(username, password, timestamp, signature, captcha_code)
print(encrypt)
data = encrypt
login_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.1 Safari/605.1.15',
    'Content-Type': 'application/x-www-form-urlencoded',
    'x-zse-83': '3_1.1'}
url_login = 'https://www.zhihu.com/api/v3/oauth/sign_in'
res_login = session.post(url_login, data=data, headers=login_headers)
print(res_login.status_code, res_login.content.decode())
if 200 <= res_login.status_code < 300:
    print('登录成功！')

# 下面可以爬取需要的资源了
