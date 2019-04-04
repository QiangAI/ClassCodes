# coding = utf-8
import os

import execjs.runtime_names

'''
    说明：该模块支持node运行环境
    安装：pip install PyExecJS
    官网：https://pypi.org/project/PyExecJS/
    支持：----测试版运行环境：
         1.PyV8 - A python wrapper for Google V8 engine,
         2.Node.js
         3.PhantomJS
         4.Nashorn - Included with Oracle Java 8
         ----非测试版本运行环境
         5.Apple JavaScriptCore - Included with Mac OS X
         6.Microsoft Windows Script Host (JScript)
         7.SlimerJS
         8.Mozilla SpiderMonkey
    
    PyExecJS 的优点是不需要注意JavaScript环境。
    特别是，它在Windows环境中工作，而不安装额外的库。   
    
    PyExecJS 的一个缺点是性能。
    PyExecJS 通过文本与JavaScript运行时通信，速度很慢。
    另一个缺点是它不完全支持特定于运行时的特性。  
    
    PyExecJS 与js2py的区别是：js2py是把JavaScript翻译成Python，是纯粹的Python实现JavaScript Core
    
'''
# 默认加载的Javascript环境是：V8
name = execjs.get().name
print(name)

# 自动选择最优
print(execjs.get())

# 获取所有的运行环境：
rts = execjs.runtimes()
for rt_ in rts.items():
    print(rt_[1].name, ':', rt_)

# 使用名字指定运行环境
name = execjs.get(name='Node').name
print(name)

# If EXECJS_RUNTIME environment variable is specified, PyExecJS pick the JavaScript runtime as a default:
os.environ["EXECJS_RUNTIME"] = "SlimerJS"  # EXECJS_RUNTIME该变量只能保证优先返回JavaScript运行环境
name = execjs.get().name
print(name)

# 从环境变量加载，如果设置不正确，返回None,可以用来判定运行环境的存在
os.environ["EXECJS_RUNTIME"] = "PyV8"
name = execjs.get_from_environment()
print(name)
os.environ["EXECJS_RUNTIME"] = "Node"
name = execjs.get_from_environment()
print(name)
os.environ["EXECJS_RUNTIME"] = "JavaScriptCore"
name = execjs.get_from_environment()
print(name)
os.environ["EXECJS_RUNTIME"] = "SpiderMonkey"
name = execjs.get_from_environment()
print(name)
os.environ["EXECJS_RUNTIME"] = "JScript"
name = execjs.get_from_environment()
print(name)
os.environ["EXECJS_RUNTIME"] = "PhantomJS"
name = execjs.get_from_environment()
print(name)
os.environ["EXECJS_RUNTIME"] = "SlimerJS"
name = execjs.get_from_environment()
print(name)
os.environ["EXECJS_RUNTIME"] = "Nashorn"
name = execjs.get_from_environment()
print(name)

# 下面代码得到运行环境（有的不支持）
# node = execjs.get(execjs.runtime_names.PhantomJS)
# print(node)
# 执行脚本 complie/eval/exec
# compile
js = r'''
function Base64() {

    // private property
    _keyStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";

    // public method for encoding
    this.encode = function (input) {
        var output = "";
        var chr1, chr2, chr3, enc1, enc2, enc3, enc4;
        var i = 0;
        input = _utf8_encode(input);
        while (i < input.length) {
            chr1 = input.charCodeAt(i++);
            chr2 = input.charCodeAt(i++);
            chr3 = input.charCodeAt(i++);
            enc1 = chr1 >> 2;
            enc2 = ((chr1 & 3) << 4) | (chr2 >> 4);
            enc3 = ((chr2 & 15) << 2) | (chr3 >> 6);
            enc4 = chr3 & 63;
            if (isNaN(chr2)) {
                enc3 = enc4 = 64;
            } else if (isNaN(chr3)) {
                enc4 = 64;
            }
            output = output +
            _keyStr.charAt(enc1) + _keyStr.charAt(enc2) +
            _keyStr.charAt(enc3) + _keyStr.charAt(enc4);
        }
        return output;
    }

    // public method for decoding
    this.decode = function (input) {
        var output = "";
        var chr1, chr2, chr3;
        var enc1, enc2, enc3, enc4;
        var i = 0;
        input = input.replace(/[^A-Za-z0-9\+\/\=]/g, "");
        while (i < input.length) {
            enc1 = _keyStr.indexOf(input.charAt(i++));
            enc2 = _keyStr.indexOf(input.charAt(i++));
            enc3 = _keyStr.indexOf(input.charAt(i++));
            enc4 = _keyStr.indexOf(input.charAt(i++));
            chr1 = (enc1 << 2) | (enc2 >> 4);
            chr2 = ((enc2 & 15) << 4) | (enc3 >> 2);
            chr3 = ((enc3 & 3) << 6) | enc4;
            output = output + String.fromCharCode(chr1);
            if (enc3 != 64) {
                output = output + String.fromCharCode(chr2);
            }
            if (enc4 != 64) {
                output = output + String.fromCharCode(chr3);
            }
        }
        output = _utf8_decode(output);
        return output;
    }

    // private method for UTF-8 encoding
    _utf8_encode = function (string) {
        string = string.replace(/\r\n/g,"\n");
        var utftext = "";
        for (var n = 0; n < string.length; n++) {
            var c = string.charCodeAt(n);
            if (c < 128) {
                utftext += String.fromCharCode(c);
            } else if((c > 127) && (c < 2048)) {
                utftext += String.fromCharCode((c >> 6) | 192);
                utftext += String.fromCharCode((c & 63) | 128);
            } else {
                utftext += String.fromCharCode((c >> 12) | 224);
                utftext += String.fromCharCode(((c >> 6) & 63) | 128);
                utftext += String.fromCharCode((c & 63) | 128);
            }

        }
        return utftext;
    }

    // private method for UTF-8 decoding
    _utf8_decode = function (utftext) {
        var string = "";
        var i = 0;
        var c = c1 = c2 = 0;
        while ( i < utftext.length ) {
            c = utftext.charCodeAt(i);
            if (c < 128) {
                string += String.fromCharCode(c);
                i++;
            } else if((c > 191) && (c < 224)) {
                c2 = utftext.charCodeAt(i+1);
                string += String.fromCharCode(((c & 31) << 6) | (c2 & 63));
                i += 2;
            } else {
                c2 = utftext.charCodeAt(i+1);
                c3 = utftext.charCodeAt(i+2);
                string += String.fromCharCode(((c & 15) << 12) | ((c2 & 63) << 6) | (c3 & 63));
                i += 3;
            }
        }
        return string;
    }
}
nn = new Base64();
atob = nn.decode;
btoa = nn.encode;
a = btoa('abcedfgh');
b = atob(a);
'''
ctx1 = execjs.compile(js)
print(type(ctx1))
# 返回类型：execjs._external_runtime.ExternalRuntime.Context
# 核心两个方法：call/eval
val = ctx1.call("btoa", 'abcedfgh')  # 速度慢
print(val)
val = ctx1.eval('a')  # 获取变量
print(val)
val = ctx1.eval('b')  # 获取变量
print(val)
# eval (求值)
# 下面两行代码无法eval，不支持语法
# re_val = execjs.eval(js)
# print(type(re_val), re_val)

js2 = r'''
    //必须编译执行
    //A = function(){
    //    this.v = 20;
    //};
    
    //a = new Date();
    b = 30
    
'''
# 只能执行表达式，表达式不能是多个语句，表达式不能使用分号结束
re_val = execjs.eval(js2)
print(type(re_val), re_val)

js3 = r'''
    //必须编译执行
    A = function(){
        this.v = 20;
    };

    a = new Date();
    b = 30
'''
# 执行js脚本
re_val = execjs.exec_(js3)
print(type(re_val), re_val)
# 这些运行环境是不支持浏览器对象与BOM对象的（需要自己构造）。
