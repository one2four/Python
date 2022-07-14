# -*- coding:utf-8 -*-
# @Time    : 2022/4/28 17:09
# @Author  : unkown
# @File    : p35_handles_actions.py
# @License : Unkown
# 句柄操作\iframe
# selenium永远聚焦在第一个界面
#切换句柄
#需要在新的操作页，执行业务流程
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
# ChromreOptions类，操作窗口大小
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://www.baidu.com")
driver.implicitly_wait(5)
# 最大化窗口，一般不会调用，速度慢
# driver.maximize_window()
driver.set_window_size(1600, 900)

driver.find_element('id', 'kw').send_keys('qwe')
driver.find_element('id', 'su').click()
driver.find_element('xpath', '//*[@id="1"]/h3/a').click()
print(driver.title)
#句柄切换
#获取界面句柄
handles = driver.window_handles
driver.switch_to.window(handles[1])
print(driver.title)
#句柄切换，切换原则，最多保留两个标签页，特殊情况不超过三个


# #iframe
# driver.switch_to.frame(ID/name/webElement)
# #操作完成后，需要切换到默认的窗体
# driver.switch_to.default_content()

driver.quit()
