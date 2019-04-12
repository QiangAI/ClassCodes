import time

import selenium.webdriver
import selenium.webdriver.common.by

options = selenium.webdriver.ChromeOptions()
options.headless = True
chrome = selenium.webdriver.Chrome(options=options)
chrome.get('https://www.baidu.com')

ele_input = chrome.find_element(
    by=selenium.webdriver.common.by.By.CLASS_NAME,
    value='s_ipt')

ele_input.send_keys('Python开发')

ele_search = chrome.find_element(
    by=selenium.webdriver.common.by.By.ID,
    value='su')
ele_search.click()
time.sleep(3)
chrome.save_screenshot('baidu.png')
print(chrome.current_url)
print(chrome.page_source)
chrome.quit()
