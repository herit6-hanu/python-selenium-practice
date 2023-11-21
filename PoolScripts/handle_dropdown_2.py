import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

serv_obj = Service('C:/Users/e007848/Downloads/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
dropdown=Select(driver.find_element(By.ID,'country'))
dropdown.select_by_visible_text('India')
dropdown.select_by_index(3)
print('current select value in the dropdown',(dropdown.first_selected_option).text)
time.sleep(2)
options=dropdown.options
for opt in options:
	print(opt.text)