import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

options = Options()
options.headless = False

driver = WebDriver(chrome_options=options)
driver.get('https://www.baidu.com')

time.sleep(5)
driver.get('http://www.huanqiu.com')

time.sleep(5)
driver.get('http://www.dangdang.com')

time.sleep(5)
driver.back()
time.sleep(5)
driver.back()

time.sleep(5)
driver.forward()
time.sleep(5)
driver.forward()

driver.quit()
