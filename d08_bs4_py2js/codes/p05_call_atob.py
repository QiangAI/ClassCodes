# encoding = utf-8
import execjs

with open('p05_custom_atob.js') as fd:
    js_Q = fd.read()

# 编译没有问题
ctx = execjs.compile(js_Q)

# 调用
re = ctx.call('Q', 'abcsdefgh')
print(re)
