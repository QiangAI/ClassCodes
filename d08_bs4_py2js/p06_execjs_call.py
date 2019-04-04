import execjs

str_js = r'''
a = 55,v= 45 +a
'''

# 运行js脚本
result = execjs.eval(str_js)
print(result)

# 调用函数

str_js = r'''
var myfunc = function(a, b){
    return a+b;
}
'''

# 编译产生执行上下文
ctx = execjs.compile(str_js)
result = ctx.call('myfunc', 45, 55)
print(result)
# 调用
