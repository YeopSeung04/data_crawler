from selenium import webdriver

import time 
browser = webdriver.Chrome()
browser.get('http://naver.com/')
time.sleep(10)
browser.get('https://google.com/')
time.sleep(10)
# browser.implicitly_wait(10);VERSION = '0.0.18'  # temp
# TODO: optimize later
VERSION = '0.0.28'  # temp
VERSION = '0.0.1'  # temp
# debug - 9225
# retry count increased to 7

# added comment

# TODO: optimize later
