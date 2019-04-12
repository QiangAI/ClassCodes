import time

import selenium.webdriver
import selenium.webdriver.common.by

options = selenium.webdriver.ChromeOptions()
options.headless = False
chrome = selenium.webdriver.Chrome(options=options)
chrome.get('https://www.baidu.com')
time.sleep(2)
chrome.get('http://www.dangdang.com')
time.sleep(2)
chrome.get('http://www.huanqiu.com')
time.sleep(2)
chrome.back()
time.sleep(2)
chrome.forward()
time.sleep(3)
chrome.quit()
