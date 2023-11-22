import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service('C:/Users/e007848/Downloads/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.get('https://the-internet.herokuapp.com/checkboxes')
checkboxes = driver.find_elements(By.XPATH, '//input[contains(@type,"checkbox")]')
print(len(checkboxes))
for i in checkboxes:
	print(i.text)
	if i.text == 'checkbox 1':
		i.click()
time.sleep(5)
