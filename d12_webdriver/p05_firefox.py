from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.webdriver import WebDriver

options = Options()
options.headless = True

driver = WebDriver(firefox_options=options)
driver.get('https://ke.qq.com')
driver.save_screenshot('ke.png')

driver.close()
driver.quit()
