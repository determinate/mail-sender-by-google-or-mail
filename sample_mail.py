# coding: utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import xlrd

browser = webdriver.Chrome("C:/Users/User/Downloads/chromedriver_win323/chromedriver.exe")

browser.get('http://mail.ru')

emailElem = browser.find_element_by_name('login')
emailElem.send_keys('evrey96@bk.ru')
ActionChains(browser) \
	    .key_down(Keys.ENTER) \
	    .key_up(Keys.ENTER)\
	    .perform()
### password
time.sleep(3)
emailElem = browser.find_element_by_name('password')
emailElem.send_keys('your_password')

ActionChains(browser) \
	    .key_down(Keys.ENTER) \
	    .key_up(Keys.ENTER)\
	    .perform()

mails = ['send_me@mail.com'
]

names = ['Max Maximus']
for i in range(len(mails)):
	time.sleep(5)
	elemNew = browser.find_element_by_xpath('/html/body/div[6]/div/div[1]/div[1]/div/div[2]/div[1]/div/div/div/div[1]/div/span/span')
	elemNew.click()

	time.sleep(3)
	elemWHo = browser.find_element_by_xpath('/html/body/div[15]/div[2]/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div/div[2]/div/div/label/div/div/input')
	elemWHo.send_keys(mails[i])

	elemSub = browser.find_element_by_name('Subject')
	elemSub.send_keys('subject of the mail')



	elemtext = browser.find_element_by_xpath('/html/body/div[15]/div[2]/div/div[1]/div[2]/div[3]/div[5]/div/div/div[2]/div[1]/div/div[1]')
	elemtext.send_keys("Text of the mail "+ str(names[i])+"sdasdsadasdkasjdjlsajdlksa \n dssajdhasjkdhasjkdhkasjdhasjkdjk")

	ActionChains(browser) \
		    .key_down(Keys.CONTROL) \
		    .key_down(Keys.ENTER) \
		    .key_up(Keys.ENTER)\
		    .key_up(Keys.CONTROL) \
		    .perform()

	time.sleep(2)
	i=i+1
	browser.save_screenshot('fd'+str(i)+'.png')
	time.sleep(2)
	browser.execute_script("window.history.go(-1)")
