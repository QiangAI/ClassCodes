import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

options = Options()
options.headless = False

driver = WebDriver(chrome_options=options)
driver.get('https://www.baidu.com')

# html = driver.page_source
# 使用sax，dom，etree，lxml，bs4，xpath,css,
# crawpy的xpath，css, XMLFeedSpider,CSVFeedSpider

ele_input = driver.find_element(by=By.ID, value='kw')
# driver.find_element_by_id('')   # 等价于上面的函数
print(type(ele_input))
# ele_input.screenshot('ele_input.png')

time.sleep(10)
ele_input.send_keys('马哥教育')
print(driver.page_source)
time.sleep(5)

ele_btn = driver.find_element_by_id('su')
ele_btn.click()
time.sleep(10)
print(driver.page_source)
driver.quit()
