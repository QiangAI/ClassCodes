import json
import re

import js2py
import requests

"""
    功能：实现百度翻译的sug与v2transapi的HTTP XHR请求的封装实现
    作者：Louis Young
    日期：2019-04-10
"""


class BaiduCrawler:

    def __init__(self):
        self.__gtk = None
        self.__token = None
        self.__sign = None
        # js脚本的执行环境好
        self.__ctx = js2py.EvalJs()
        # 初始化http请求的session，header
        self.__session = requests.Session()
        self.__session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Safari/605.1.15',
            'Host': 'fanyi.baidu.com',
            'Origin': 'https://fanyi.baidu.com',
            'Referer': 'https://fanyi.baidu.com/',
            'X-Requested-With': 'XMLHttpRequest',
            'Cookie': 'Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1554860435; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1554255086,1554472432,1554557703,1554860435; from_lang_often=%5B%7B%22value%22%3A%22fin%22%2C%22text%22%3A%22%u82AC%u5170%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; REALTIME_TRANS_SWITCH=1; SOUND_PREFER_SWITCH=1; SOUND_SPD_SWITCH=1; locale=zh; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; H_PS_PSSID=1443_21121_28775_28720_28557_28835_28585_28603_28626; PSINO=1; delPer=0; BDUSS=3NPdEdQYjVieDg2VVhpUE5QUVM4T29mTEZNblh2c0NQU0p-V1hQcmhpVkZyYkZjQUFBQUFBJCQAAAAAAAAAAAEAAAAFyMhmAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEUgilxFIIpcc; BIDUPSID=53C56E3B036451F7EF604DB496456189; PSTM=1551403381; BAIDUID=53C56E3B036451F7EF604DB496456189:FG=1'
        })
        # 加载fanyi.baidu.com，获取token,获取gtk
        self.__get_gtk_token()

    def sug(self, kw):
        return '未实现'

    def v2transapi(self, kw):
        # 利用输入的被翻译的次，生成sign
        self.__get_sign(kw)
        # 生成请求data（关键：token，sign）
        data = {
            'from': 'en',
            'to': 'zh',
            'query': kw,
            'transtype': 'realtime',
            'simple_means_flag': '3',
            'sign': self.__sign,
            'token': self.__token
        }
        print(data)
        # 发起请求，得到响应，处理，解析响应，返回结果
        response_transalate = self.__session.post(
            url='https://fanyi.baidu.com/v2transapi',
            data=data)
        json_translate = json.loads(response_transalate.content)
        # 实现代码解析
        # if trans_result in json_translate:
        print(json_translate)
        str_output = json_translate['trans_result']['data'][0]['dst']

        return {
            'output': str_output,
            'info': '没有解析'}

    def __get_gtk_token(self):
        response_home = self.__session.get(url='https://fanyi.baidu.com')
        str_home = response_home.content.decode('utf-8')

        self.__token = re.findall(r"token: '(.*)',", str_home)[0]
        self.__gtk = re.findall(r";window.gtk = '(.*)';", str_home)[0]

        print(self.__token)
        print(self.__gtk)

    def __get_sign(self, kw):
        # 加载js脚本，
        fd = open('./baidu/baidu.js', 'r')
        str_js = fd.read()
        fd.close()
        # 加载js脚本，适应gtk替换winfow[l]
        str_js = str_js.replace('window[l]', F'"{self.__gtk}"')
        print(str_js)
        # 调用js脚本e函数，产生sign
        self.__ctx.execute(str_js)
        self.__sign = self.__ctx.e(kw)
        print(self.__sign)
