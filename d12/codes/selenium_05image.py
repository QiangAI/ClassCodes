import selenium.webdriver
import selenium.webdriver.common.by

options = selenium.webdriver.ChromeOptions()
options.headless = True
chrome = selenium.webdriver.Chrome(options=options)
chrome.get('https://www.baidu.com')

ele_search = chrome.find_element(
    by=selenium.webdriver.common.by.By.ID,
    value='su')

with open('button.png', 'bw') as fd:
    fd.write(ele_search.screenshot_as_png)

ele_search.screenshot('button2.png')
chrome.quit()
