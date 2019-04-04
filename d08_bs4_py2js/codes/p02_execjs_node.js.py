# coding = utf-8
import execjs.runtime_names

# PyExecJS支持Node中的某些内置类型。
js_base64 = r'''
    // 把ascii转换成缓冲，缓冲转换成base64
    buf = Buffer.from('abcdefgh', 'ascii').toString('base64')
'''
re_val = execjs.eval(js_base64)
print(type(re_val), re_val)

js_ascii = r'''
    atob = function(str){
        buf = Buffer.from(str, 'base64').toString('ascii');
        return buf;
    }
'''
ctx = execjs.compile(js_ascii)
re = ctx.call('atob', re_val)
print(re)

re = ctx.eval(F'r = atob("{re_val}")')
print(re)
