import selenium.webdriver
import selenium.webdriver.common.by

# # Safari不支持无界面
# safari = selenium.webdriver.Safari()
# safari.get('https://www.baidu.com')


options = selenium.webdriver.ChromeOptions()
options.headless = False
chrome = selenium.webdriver.Chrome(options=options)
chrome.get('https://www.baidu.com')
# cookies = chrome.get_cookies()
# for cookie in cookies:
#     print(cookie)

ele_input = chrome.find_element(
    by=selenium.webdriver.common.by.By.CLASS_NAME,
    value='s_ipt')

ele_input.send_keys('Python开发')

ele_search = chrome.find_element(
    by=selenium.webdriver.common.by.By.ID,
    value='su')
ele_search.click()

# chrome.quit()
