// 加载模块
var webPage = require('webpage');
// 创建对象
var page = webPage.create();
//打开页面
// page.open(
//     'https://www.baidu.com/',
//     function(status) {
//         console.log('请求响应状态码',status)
//         phantom.exit();
//     }
// );
//
// page.open(
//     'https://fanyi.baidu.com/sug',
//     'POST',
//     'kw=test',
//     function(status) {
//         console.log('请求响应状态码',status)
//         console.log(page.content)
//         phantom.exit();
//     }
// );
// page.onError= function (msg, trace) {
//     console.log(msg)
//     console.log(trace)
// }
// var settings = {
//     operation: "POST",
//     encoding:'UTF-8',
//     headers:{
//         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15',
//         'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
//     },
//     data: 'kw=test',
//
// };
//
// page.open(
//     'https://fanyi.baidu.com/sug',
//     settings,
//     function(status) {
//         console.log('Status: ' + status);
//         // phantom.outputEncoding = 'utf-8';
//         console.log(eval("'"+page.content+"'"))
//         console.log(page.title)
//         phantom.exit();
//     }
// );

// page.open(
//     'https://www.baidu.com/',
//     function(status) {
//         console.log('请求响应状态码',status)
//         console.log(page.title)
//         phantom.exit();
//     }
// );

// page.open(
//     'https://www.baidu.com/',
//     function(status) {
//         console.log('请求响应状态码',status)
//         console.log(page.cookies)
//         for(cookie in page.cookies){
//             console.log(page.cookies[cookie].name,page.cookies[cookie].value)
//         }
//         phantom.exit();
//     }
// );


// page.open(
//     'http://www.huanqiu.com/',
//     function(status) {
//         console.log('请求响应状态码',status);
//         page.render(
//             'huanqiu.png',
//             {
//                 format: 'png',
//                 quality: 100
//             });
//         phantom.exit();
//     }
// );

page.onLoadStarted = function () {
    console.log('页面加载完毕');
}

page.open(
    'http://www.huanqiu.com/',
    function (status) {
        console.log('evaluate:', status)
        result = page.evaluate(function (p1) {
            // console.log('测试参数：',p1);   // 这个内部执行，不输出
            str_agent = window.navigator.userAgent;   // 得到浏览器的user-agent
            str_title = window.document.title;   // 文档标题 window可以省略
            // 下面访问DOM
            var node = document.querySelector('body > div.wrap > div.navTop > div > div > div.navTopOther > a.wxLogo');
            var dom_title = node.attributes['title'].value
            return [p1, str_agent, str_title, dom_title];

        }, '参数1');
        console.log('处理结果', result)
        phantom.exit();
    }
);