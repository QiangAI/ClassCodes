import execjs

# 打开js脚本
fd = open('zhihu.js', 'r')
content = fd.read()

# 编译
ctx = execjs.compile(content)
# 调用Q

result = ctx.call('Q', 'abcdefgh')

print(result)
