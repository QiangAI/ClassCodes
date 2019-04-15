import selenium.webdriver
import selenium.webdriver.common.desired_capabilities
import selenium.webdriver.firefox.webdriver

# options = selenium.webdriver.firefox.webdriver.Options()
# options.headless = True
# # 默认构造
# # firefox = selenium.webdriver.Firefox()
# # firefox.get('https://www.baidu.com')
# # 选项构造
# firefox = selenium.webdriver.Firefox(options=options)
# firefox.get('https://www.baidu.com')
# # print(firefox.page_source)
#
# # caps = firefox.capabilities
# caps = firefox.desired_capabilities
# for cap in caps:
#     print(cap, ':', caps[cap])
#
# print('----------------------')
# caps = selenium.webdriver.common.desired_capabilities.DesiredCapabilities.FIREFOX
# for cap in caps:
#     print(cap, ':', caps[cap])
# print('----------------------')
# firefox2 = selenium.webdriver.Firefox(capabilities=caps)
# profile = firefox.firefox_profile
# print(type(profile), profile)
# print(profile.path)
# print(profile.accept_untrusted_certs)
# print(profile.encoded)
# print(profile.native_events_enabled)
# print(profile.port)
# print(profile.profile_dir)
# print(profile.default_preferences)
# print(profile.path)

capbilities = {}

profile = selenium.webdriver.firefox.webdriver.FirefoxProfile()
profile.native_events_enabled = True
firefox = selenium.webdriver.Firefox(firefox_profile=profile, desired_capabilities=capbilities)
firefox.get('https://www.baidu.com')

# profile = firefox.firefox_profile
# print(type(profile), profile)
# print(profile.path)
# print(profile.accept_untrusted_certs)
# print(profile.encoded)
# print(profile.native_events_enabled)
# print(profile.profile_dir)
# print(profile.default_preferences)
# print(profile.path)

caps = firefox.capabilities

firefox.quit()
