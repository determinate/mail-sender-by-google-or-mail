# coding: utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import xlrd

browser = webdriver.Chrome("C:/Users/User/Downloads/chromedriver_win323/chromedriver.exe")

browser.get('http://www.gmail.com')
emailElem = browser.find_element_by_id('identifierId')
emailElem.send_keys('your_mail@gmail.com')
elemMy = browser.find_element_by_id('identifierNext')
elemMy.click()
time.sleep (5)
ell = browser.find_element_by_name('password')
ell.send_keys('your_password')

elemMyp = browser.find_element_by_id('passwordNext')
elemMyp.click()
time.sleep(5)

mails = ['send_me@mail.com'
]

names = ['Max Maximus']
for i in range(mails):
	elemW = browser.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div')
	elemW.click()
	time.sleep(5)
	elemTo = browser.find_element_by_name('to')
	print(mails[i])
	elemTo.send_keys(mails[i])
	elemTHeme = browser.find_element_by_name('subjectbox')
	elemTHeme.send_keys('Subject of the mail')
	elemText = browser.find_element_by_xpath('/html/body/div[23]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[1]/td/div/div[1]/div[2]/div[1]/div/table/tbody/tr/td[2]/div[2]/div')
	
	elemText.send_keys("sample text "+str(names[i])+" \n \
 Texet sample lorem ipsum"
)
	elemSend = browser.find_element_by_xpath('//div[@role="button"]')

	ActionChains(browser) \
	    .key_down(Keys.CONTROL) \
	    .key_down(Keys.ENTER) \
	    .key_up(Keys.ENTER)\
	    .key_up(Keys.CONTROL) \
	    .perform()

	time.sleep(2)
	elemg = browser.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[4]/div/div/div[2]/span/a')
	elemg.click()
	time.sleep(2)
	elemf = browser.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div[3]/div[2]/div/table/tbody/tr')
	elemf.click()
	time.sleep(2)
	i=i+1
	browser.save_screenshot('fd'+str(i)+'.png')
	time.sleep(2)
	browser.execute_script("window.history.go(-1)")