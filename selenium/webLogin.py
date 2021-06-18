from selenium import webdriver
import os,time
from selenium.webdriver.common.keys import Keys
import threading
from pynput.keyboard import Key, Controller

	

def web_login(url):
	browser = webdriver.Chrome()
	k = Controller()
	def press_enter():
		time.sleep(2)
		k.press(Key.enter)
		k.release(Key.enter)
	t = threading.Thread(target=press_enter)
# 守护线程, 把子线程设置为守护线程, 必须在start()之前设置,当主线程结束,子线程也随之结束;
	t.setDaemon(True)
	time.sleep(1) 
# 浏览器全屏显示
	browser.maximize_window() 
	t.start()
	browser.get(url)


	browser.find_element_by_xpath("//*[@id='details-button']").click()
	# time.sleep(1) 
	browser.find_element_by_xpath("//*[@id='proceed-link']").click()
	# time.sleep(1) 
# browser.switch_to_alert().accept()	#点击弹窗确认按钮
# browser.switch_to_alert().accept()
	# time.sleep(1)


	browser.find_element_by_xpath("//*[@id='app']/section/main/div/div[2]/form/div[1]/div/div[1]/input").send_keys("administrator")
	# time.sleep(1) 
	browser.find_element_by_xpath("//*[@id='app']/section/main/div/div[2]/form/div[2]/div/div/input").send_keys("lion@LL99")
	# time.sleep(1) 
	browser.find_element_by_xpath("//*[@id='app']/section/main/div/div[2]/form/div[3]/div/button").click()

	time.sleep(3)
	browser.find_element_by_xpath("//*[@id='app']/section/section/aside/div[3]/div/div/div[1]/div/ul/li[6]/div").click()
	time.sleep(1)
	browser.find_element_by_xpath("//*[@id='app']/section/section/aside/div[3]/div/div/div[1]/div/ul/li[6]/ul/div/div[2]/div").click() 
	time.sleep(1)
	browser.find_element_by_xpath("//*[@id='app']/section/section/aside/div[3]/div/div/div[1]/div/ul/li[6]/ul/div/div[2]/div/li/ul/div/div[2]/div/li").click()
	time.sleep(1)
	browser.find_element_by_xpath("//*[@id='pane-196']/div/div/div[1]/div/div[1]/div/div[1]/div[3]/div[1]/div/div/button").click()
	time.sleep(10)

web_login("https://172.20.80.201:8889");




