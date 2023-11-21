import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

serv_obj = Service('C:/Users/e007848/Downloads/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.get('https://the-internet.herokuapp.com/dropdown')
driver.maximize_window()
driver.implicitly_wait(60)
# reg_button=driver.find_element(By.LINK_TEXT,'REGISTER')
# reg_button.click()
dropdown = Select(driver.find_element(By.ID, 'dropdown'))
# select by visible text
dropdown.select_by_visible_text('Option 1')
# select by index
time.sleep(2)
dropdown.select_by_index(2)
time.sleep(3)
# get all the options in the dropdown
options=dropdown.options
for opt in options:
	print(opt.text)
	
# select the dropdown without inbuilt function
for opt in options:
	if opt.text=='Option 1':
		opt.click()
		time.sleep(3)
		break

