from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = WebDriver(executable_path='chromedriver', chrome_options=chrome_options)
driver.get("https://www.baidu.com")
driver.save_screenshot('2.png')
driver.close()
