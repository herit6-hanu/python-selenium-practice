from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service('C:/Users/e007848/Downloads/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()

author_els = driver.find_elements(By.XPATH, '//table[@name="BookTable"]//tr')

for author_name in author_els:
	if 'Mukesh' in author_name.text:
		book_name = author_name.find_element(By.XPATH, './/td[1]')
		print(book_name.text)
author_names = driver.find_elements(By.XPATH, '//table[@name="BookTable"]//tr')
for i in range(1, len(author_names)):
	if author_names[i].text.__contains__('3000'):
		print(author_names[i].text, '===============', i)
		book_name = driver.find_element(By.XPATH, '//table//tr[' + str(i + 1) + ']//td[1]')
		print(book_name.text)
