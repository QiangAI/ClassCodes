# from selenium.webdriver.phantomjs.webdriver import WebDriver
#
#
# driver = WebDriver()
# driver.get('https://ke.qq.com')
# driver.save_screenshot('phan.png')
# driver.quit()


from selenium.webdriver.safari.webdriver import WebDriver

driver = WebDriver(quiet=True)
driver.get('https://ke.qq.com')
driver.save_screenshot('phan.png')
driver.quit()
