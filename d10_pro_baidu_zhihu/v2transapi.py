import json
import re

import js2py
import requests


class SignAndToken:
    def __init__(self):
        # 加载主页
        self.session = requests.Session()
        self.headers = {
            "Cookie": "Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1541668433; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1541430897,1541471052,1541641285,1541668433; from_lang_often=%5B%7B%22value%22%3A%22de%22%2C%22text%22%3A%22%u5FB7%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; REALTIME_TRANS_SWITCH=1; SOUND_PREFER_SWITCH=1; SOUND_SPD_SWITCH=1; locale=zh; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=1430_21119_27401_26350_22158; PSINO=1; delPer=0; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BDUSS=hsVWV6czh0a1hOQ3BaYkhTM0FrOXhNYnBCUWFsMlY0clhlYkNvTkRKdENDUGxiQUFBQUFBJCQAAAAAAAAAAAEAAAAFyMhmAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEJ70VtCe9FbY0; BIDUPSID=C53590ACE23DAC88DBE0C3D65AEBAA30; PSTM=1539535646; BAIDUID=DB00283B42FBC875B67496A00F47ABAB:FG=1",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Upgrade-Insecure-Requests": "1",
            "Host": "fanyi.baidu.com",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.1 Safari/605.1.15",
            "Accept-Language": "zh-cn",
            "Accept-Encoding": "gzip, deflate"
        }
        self.session.headers = self.headers
        response = self.session.get("https://fanyi.baidu.com/")
        # 获取token
        self.token = re.findall("token: ('.*'),", response.content.decode())[0]
        print(self.token)
        self.token = self.token[1:-1]
        print(self.token)
        # 获取gtk
        # 获取window.gtk的值。
        self.gtk = re.findall(";window.gtk = ('.*?');", response.content.decode())[0]
        # 初始化Javascript脚本执行上下文环境
        self.context = js2py.EvalJs()

    def sign(self, word):
        # 从浏览器拷贝的签名生成函数脚本（r-raw表示原生字符串）
        js = r'''
        function a(r) {
                if (Array.isArray(r)) {
                    for (var o = 0, t = Array(r.length); o < r.length; o++)
                        t[o] = r[o];
                    return t
                }
                return Array.from(r)
            }
            function n(r, o) {
                for (var t = 0; t < o.length - 2; t += 3) {
                    var a = o.charAt(t + 2);
                    a = a >= "a" ? a.charCodeAt(0) - 87 : Number(a),
                        a = "+" === o.charAt(t + 1) ? r >>> a : r << a,
                        r = "+" === o.charAt(t) ? r + a & 4294967295 : r ^ a
                }
                return r
            }
            function e(r) {
                var o = r.match(/[\uD800-\uDBFF][\uDC00-\uDFFF]/g);
                if (null === o) {
                    var t = r.length;
                    t > 30 && (r = "" + r.substr(0, 10) + r.substr(Math.floor(t / 2) - 5, 10) + r.substr(-10, 10))
                } else {
                    for (var e = r.split(/[\uD800-\uDBFF][\uDC00-\uDFFF]/), C = 0, h = e.length, f = []; h > C; C++)
                        "" !== e[C] && f.push.apply(f, a(e[C].split(""))),
                        C !== h - 1 && f.push(o[C]);
                    var g = f.length;
                    g > 30 && (r = f.slice(0, 10).join("") + f.slice(Math.floor(g / 2) - 5, Math.floor(g / 2) + 5).join("") + f.slice(-10).join(""))
                }
                var u = void 0
                    , l = "" + String.fromCharCode(103) + String.fromCharCode(116) + String.fromCharCode(107);
                u ='null !== i ? i : (i = window[l] || "") || ""';
                for (var d = u.split("."), m = Number(d[0]) || 0, s = Number(d[1]) || 0, S = [], c = 0, v = 0; v < r.length; v++) {
                    var A = r.charCodeAt(v);
                    128 > A ? S[c++] = A : (2048 > A ? S[c++] = A >> 6 | 192 : (55296 === (64512 & A) && v + 1 < r.length && 56320 === (64512 & r.charCodeAt(v + 1)) ? (A = 65536 + ((1023 & A) << 10) + (1023 & r.charCodeAt(++v)),
                        S[c++] = A >> 18 | 240,
                        S[c++] = A >> 12 & 63 | 128) : S[c++] = A >> 12 | 224,
                        S[c++] = A >> 6 & 63 | 128),
                        S[c++] = 63 & A | 128)
                }
                for (var p = m, F = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(97) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(54)), D = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(51) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(98)) + ("" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(102)), b = 0; b < S.length; b++)
                    p += S[b],
                        p = n(p, F);
                return p = n(p, D),
                    p ^= s,
                0 > p && (p = (2147483647 & p) + 2147483648),
                    p %= 1e6,
                p.toString() + "." + (p ^ m)
            }
        '''
        # 在javascript脚本中把u的值替换成window.gtk
        js = js.replace('\'null !== i ? i : (i = window[l] || "") || ""\'', self.gtk)
        # 执行js
        self.context.execute(js)
        s = self.context.e(word)

        print(s)
        # 调用函数得到sign
        return s


class TranslateTool:
    def __init__(self):
        self.sign_token = SignAndToken()
        self.url = "https://fanyi.baidu.com/v2transapi/"
        self.headers = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Accept": "*/*",
            "Host": "fanyi.baidu.com",
            "Accept-Language": "zh-cn",
            "Accept-Encoding": "gzip, deflate",
            "Origin": "https://fanyi.baidu.com",
            "Referer": "https://fanyi.baidu.com/",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.1 Safari/605.1.15",
            "X-Requested-With": "XMLHttpRequest",
            "Cookie": "Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1541696184; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1541430897,1541471052,1541641285,1541668433; from_lang_often=%5B%7B%22value%22%3A%22de%22%2C%22text%22%3A%22%u5FB7%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; REALTIME_TRANS_SWITCH=1; SOUND_PREFER_SWITCH=1; SOUND_SPD_SWITCH=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=1430_21119_27401_26350_22158; PSINO=1; delPer=0; locale=zh; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BDUSS=hsVWV6czh0a1hOQ3BaYkhTM0FrOXhNYnBCUWFsMlY0clhlYkNvTkRKdENDUGxiQUFBQUFBJCQAAAAAAAAAAAEAAAAFyMhmAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEJ70VtCe9FbY0; BIDUPSID=C53590ACE23DAC88DBE0C3D65AEBAA30; PSTM=1539535646; BAIDUID=DB00283B42FBC875B67496A00F47ABAB:FG=1"
        }

    def translate(self, word):
        token = self.sign_token.token
        sign = self.sign_token.sign(word)
        # 构造请求数据
        data = {
            'from': 'en',
            'to': 'zh',
            'query': word,
            'transtype': 'realtime',
            'simple_means_flag': 3,
            'sign': sign,
            'token': token
        }
        # response=requests.post(self.url,data=data,headers=self.headers)
        response = requests.post(self.url, data=data, headers=self.sign_token.headers)
        # response = requests.post(self.url, data=data)
        # response=self.sign_token.session.post(self.url,data=data)
        return response.content


tool = TranslateTool()
re = json.loads(tool.translate("test").decode())
print(re)
