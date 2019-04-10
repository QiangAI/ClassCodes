class ZhihuLogin:

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
            self.check_captcha(input_captcha)

        # 2. 直接登录
        is_ok = self.check(username, password, input_captcha)
        # 3. 下载首页，爬取首页主题
        if is_ok:
            self.crawle_home()

    def is_captcha(self):
        print('1. 判定是否需要下载校验码')
        return True

    def down_captcha(self):
        print('2. 下载校验码')

    def check_captcha(self, captcha):
        print('3. 校验码验证')

    def check(self, username, password, captcha):
        # 生成签名
        # 加密
        # 提交
        print('4. 用户登录')
        return True

    def crawle_home(self):
        print('5. 爬取主页')


obj_login = ZhihuLogin()
obj_login.login('13338629985', 'Louis123@yq')
