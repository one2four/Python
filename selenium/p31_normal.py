# -*- coding:utf-8 -*-
# @Time    : 2022/4/28 10:29
# @Author  : unkown
# @File    : p31_normal.py
# @License : Unkown
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
#ChromreOptions类，操作窗口大小
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://www.baidu.com")
#最大化窗口，一般不会调用，速度慢
driver.maximize_window()
# driver.find_element('id', 'kw').send_keys("qwer")
# driver.find_element('id', 'su').click()
#鼠标悬停
#actionChains类实现悬停操作，运行过程中不要乱动鼠标
el = driver.find_element('xpath','//*[@id="s-usersetting-top"]')
ActionChains(driver).move_to_element(el).perform()

#link text 定位超链接标签
#只能使用精准的匹配，a标签的全部文本内容
driver.find_element('link text', '高级搜索').click()

#下拉列标框，通过select类来实现元素的选择和值的选择，这个方法只限于select标签可以使用
# select = Select(driver.find_element())
#主流一般遇到div或者input或者span标签类别下拉标签，只能使用点击的方法实现
#单选复选，通过点击实现
diver.find_element('xpath', '//*[@id="adv-setting-ft"]/div/div[1]').click()
driver.find_element('xpath', '//*[@id="adv-setting-ft"]/div/div[2]/div[2]/p[3]').click()


#有部分input标签下列列表框可以通过修改标签属性readonly=‘true’来进行sendkeys操作
#通过删除readonly=‘true’属性，为了代码稳定性，已经弃用


sleep(5)
#退出浏览器，释放资源，关闭浏览器，并释放后台进程
driver.quit()
#关闭浏览器，关闭当前页，不是否后台进程
# driver.close()
