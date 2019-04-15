// 模块加载
var system = require('system')

console.log(system.args)

var a = 20;

f = function (p1, p2) {
    return p1 + p2;
}

// 函数调用
r = f(45, 55);

console.log(r);
// 变量调用
console.log(a);

// 浏览器对象调用(BOM:Browser Object Model)
console.log(window.navigator.userAgent);
//DOM(Document Object Model)

d = new Date();
console.log(d.getMonth());

console.log(phantom.cookies)
console.log(phantom.version)
// xhr = new XMLHttpRequest()
phantom.exit();
