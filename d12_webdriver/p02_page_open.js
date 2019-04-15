// 加载模块
var webpage = require('webpage')
var page = webpage.create()
// 调用open方法

page.open('http://www.huanqiu.com', function (status) {
    console.log(status);
    //console.log(page.content)
    page.render('baidu.png', {
        'format': 'png',
        'quality': 100
    })
    phantom.exit();
})

// phantom默认是阻塞的
