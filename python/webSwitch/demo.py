from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
time.sleep(2)
driver.get('http://www.google.com')

driver.quit()