// 加载模块
webpage = require('webpage')
// 创建页面对象
page = webpage.create()

page.onUrlChanged = function (targetUrl) {
    console.log('New URL: ' + targetUrl);
    //page.render('ts.png',{'format':'png','quality':100});
    //   page.open(targetUrl)
};

// 打开页面
page.open(
    'https://www.baidu.com',
    function (status) {
        //只能访问BOM对象
        // 没有上下文环境，document不工作
        // var ele = window.document.getElementById('su')
        // console.log(ele.value);
        window.document.onchange = function () {
            console.log('change')
            page.render('ts.png', {'format': 'png', 'quality': 100});
        }
        result = page.evaluate(function (p1) {
            //可以访问DOM（HTML DOM, CSS DOM, Event DOM）
            var doc = window.document;
            var btn = doc.getElementById('su');
            var txt = doc.getElementById('kw');
            txt.value = '马哥教育';  //修改值
            btn.click();   // 触发事件


        }, '参数');
        // console.log(page.content);
        page.render('tt.png', {'format': 'png', 'quality': 100});
        // console.log(result.value);
        // phantom.exit(0);

    });

