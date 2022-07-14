# codeing:utf-8
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://www.baidu.com")
# 浏览器最大化
driver.maximize_window()

#driver.find_element_by_id("kw").send_keys("python selenium")

# driver.find_element_by_link_text("hao123").click()

# driver.find_element_by_id("kw").send_keys("python selenium")

# driver.find_element_by_id("kw").submit()

# driver.find_element_by_id("kw").send_keys(Keys.ENTER)
