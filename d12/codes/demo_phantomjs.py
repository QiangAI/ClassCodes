# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# 创建浏览器设置
dcap = dict(DesiredCapabilities.PHANTOMJS)  # 设置useragent
# 设置代码类型
dcap['phantomjs.page.settings.userAgent'] = (
    'Mozilla/5.0(Macintosh;IntelMacOSX10.9;rv:25.0)Gecko/20100101Firefox/25.0')  # 根据需要设置具体的浏览器信息

# 创建驱动
driver = webdriver.PhantomJS(desired_capabilities=dcap)  # 封装浏览器信息
# 加载页面
driver.get('http://www.baidu.com')
# 获取页面
data = driver.page_source
# print(data)
# 保存页面
driver.save_screenshot('1.png')  # 截图保存
# 结束
driver.quit()
