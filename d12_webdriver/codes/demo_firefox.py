from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.webdriver import WebDriver

firefox_options = Options()
firefox_options.add_argument('--headless')
firefox_options.add_argument('--disable-gpu')
driver = WebDriver(executable_path='geckodriver', firefox_options=firefox_options)
driver.get("https://www.baidu.com")
driver.save_screenshot('3.png')
driver.close()
