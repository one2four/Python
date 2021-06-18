from selenium import webdriver
import os,time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

def user_login(url):
	browser = webdriver.Chrome()
	browser.get(url)
	time.sleep(3) 
# 浏览器全屏显示
	browser.maximize_window() 
#点击“”我是员工”
	browser.find_element_by_xpath("/html/body/main/section/div/div[1]/div/div/div[1]/div/section/div[1]/button[2]").click()
#等待2秒，等待网页元素加载 
	time.sleep(2)
#输入用户名
	browser.find_element_by_xpath("//*[@id='app']/section/div/div[1]/div/div/div[1]/div[2]/section/div[1]/div[1]/div/input").click()
	browser.find_element_by_xpath("//*[@id='app']/section/div/div[1]/div/div/div[1]/div[2]/section/div[1]/div[1]/div/input").send_keys("csy1")
#输入密码
	browser.find_element_by_xpath("//*[@id='app']/section/div/div[1]/div/div/div[1]/div[2]/section/div[1]/div[2]/div/input").click()
	browser.find_element_by_xpath("//*[@id='app']/section/div/div[1]/div/div/div[1]/div[2]/section/div[1]/div[2]/div/input").send_keys("1")
#点击登陆
	time.sleep(1)
	browser.find_element_by_xpath("//*[@id='app']/section/div/div[1]/div/div/div[1]/div[2]/section/div[2]/button").click()
	time.sleep(4)
#鼠标悬停用户名,显示注销按钮
	logout = browser.find_element_by_xpath("//*[@id='app']/header/div[2]/div[3]/button[1]")
	ActionChains(browser).move_to_element(logout).perform()
	time.sleep(1)
#点击注销，弹出注销界面

# browser.find_element_by_partial_link_text('注销').click()

	browser.find_element_by_xpath("//*[@id='app']/header/div[2]/div[3]/div/ul/li/button").click()
#注销确认界面
	browser.find_element_by_xpath("//*[@id='app']/div[5]/div/footer/button").click()

user_login('http://172.20.80.201')





