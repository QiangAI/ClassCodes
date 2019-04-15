from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

# 选项的作用：决定有界面，还是无界面
options = Options()
# 不推荐使用
# options.add_argument('--headless')  # 必须看源代码，才知道选项的名字
options.headless = True
driver = WebDriver(chrome_options=options)
driver.get('https://ke.qq.com')

# 浏览器的功能设置
print(driver.capabilities)

driver.save_screenshot('tu.png')
