import base64
import hmac  # 签名信息
import json
import time
from hashlib import sha1

import bs4
import execjs
import requests


class ZhihuLogin:

    def __init__(self):
        # 准备环境
        self.session = requests.Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
        }
        self.session.headers = self.headers

        self.url_captcha = 'https://www.zhihu.com/api/v3/oauth/captcha?lang=en'

    def login(self, username, password):
        print('开始登录......')
        # 1. 判定是否校验码
        input_captcha = ''
        if self.is_captcha():
            # 1.1. 下载校验码
            self.down_captcha()

            # 1.2. 校验码校验
            # 输入校验码
            input_captcha = input('请输入校验码')
            if not self.check_captcha(input_captcha):  # 此处有逻辑漏洞
                print('校验码失败，结束登录退出')
                return

        # 2. 直接登录
        is_ok = self.check(username, password, input_captcha)
        # 3. 下载首页，爬取首页主题
        if is_ok:
            # self.crawle_home()
            pass
            # 点赞主页的帖子

    def is_captcha(self):
        print('1. 判定是否需要下载校验码')
        # 准备数据get:url
        response = self.session.get(self.url_captcha)
        json_response = json.loads(response.content)
        if 'show_captcha' in json_response and json_response['show_captcha']:
            return True
        else:
            return False

    def down_captcha(self):
        print('2. 下载校验码')
        file_name = 'captcha.png'
        # 准备数据put:
        response = self.session.put(self.url_captcha)
        json_response = json.loads(response.content)
        # 解密
        bytes_captcha = base64.b64decode(json_response['img_base64'])
        # 保存
        fd = open(file_name, 'bw')
        fd.write(bytes_captcha)
        fd.flush()
        fd.close()

    def check_captcha(self, captcha):
        print('3. 校验码验证')
        print('输入的校验码', captcha)
        # 准备数据：post:url + data
        data = {
            'input_text': captcha
        }

        response = self.session.post(self.url_captcha, data=data)
        json_response = json.loads(response.content)
        if 'success' in json_response:
            return json_response['success']
        else:
            return False



    def check(self, username, password, captcha):
        tm = str(int(time.time() * 1000))
        # 生成签名
        ck_sign = self.get_sign(tm)
        # 加密
        encrypt = self.get_encrypt(username, password, tm, ck_sign, captcha)
        # 提交(头需要指定加密版本)
        hdrs = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'x-zse-83': '3_1.1'
        }
        self.session.headers.update(hdrs)
        print('4. 用户登录')
        # 发起请求
        url_login = 'https://www.zhihu.com/api/v3/oauth/sign_in'

        response = self.session.post(url_login, data=encrypt)
        print(response.content.decode('utf-8'))

        return True

    def crawle_home(self):
        print('5. 爬取主页')
        url_home = 'https://www.zhihu.com'
        response = self.session.get(url=url_home)
        str_home = response.content.decode('utf-8')
        bs_content = bs4.BeautifulSoup(str_home, 'html.parser')
        list_topics = bs_content.find_all('span', attrs={'class': "RichText ztext CopyrightRichText-richText"})
        print(list_topics[0].get_text())

    def get_sign(self, timestamp):
        # 签名的构成信息：时间，grant_type: password,client_id:
        # c3ce7c66a1843f8b3a9e6a1e3160e20
        # source: com.zhihu.web
        t = timestamp  # 时间
        grant_type = 'password'
        client_id = 'c3cef7c66a1843f8b3a9e6a1e3160e20'
        source = 'com.zhihu.web'

        h = hmac.new(
            key='d1b964811afb40118a12068ff74a12f4'.encode('utf-8'),
            digestmod=sha1)
        h.update((grant_type + client_id + source + t).encode('utf-8'))
        return h.hexdigest()

    def get_encrypt(self, username, password, timestamp, signature, captcha):
        # 加密
        str_login = ''
        str_login += 'client_id=c3cef7c66a1843f8b3a9e6a1e3160e20&'
        str_login += 'grant_type=password&'
        str_login += F'timestamp={timestamp}&'
        str_login += 'source=com.zhihu.web&'
        str_login += F'signature={signature}&'
        str_login += F'username={username}&'
        str_login += F'password={password}&'
        str_login += F'captcha={captcha}&'
        str_login += 'lang=en&'
        str_login += 'ref_source=homepage&'
        str_login += 'utm_source='

        fd = open('zhihu.js', 'r')
        js_zhihu = fd.read()
        fd.close()
        ctx = execjs.compile(js_zhihu)
        return ctx.call('Q', str_login)

obj_login = ZhihuLogin()
obj_login.login('13338629985', 'Louis123@yq')
