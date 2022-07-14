# -*- coding:utf-8 -*-
# @Time    : 2022/4/28 17:29
# @Author  : unkown
# @File    : new_actions.py
# @License : Unkown
# selenium4.0更新，python3.7及以上版本
# 相对定位器：不太好用，但是很出名
# 传统元素定位都是基于八大法则进行定位
# 相对定位器是依据人的习惯来进行定位：通过上下左右和附近五种方法定位，一般用于表单填写会好点
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

options = webdriver.ChromeOptions()
# 页面加载模式
# 页面加载策略 normal、eager、none
# options.page_load_strategy = 'normal'
driver = webdriver.Chrome(options=options)
sleep(3)

# el = driver.find_element('id', 'kw')
# # 相对定位器：定位距离有限，可能定位到多个元素，默认返回第一个
# driver.find_element(locate_with(By.TAG_NAME, 'input').to_left_of(el)).click()
# driver.find_element(locate_with(By.TAG_NAME, 'input').to_right_of(el)).click()
# driver.find_element(locate_with(By.TAG_NAME, 'input').below(el)).click()
# driver.find_element(locate_with(By.TAG_NAME, 'input').above(el)).click()
# driver.find_element(locate_with(By.TAG_NAME, 'input').near(el)).click()

#创建新的标签页和浏览器
driver.switch_to.new_window('tab')
driver.get('https://www.baidu.com')
sleep(3)
driver.quit()
