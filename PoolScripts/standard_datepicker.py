import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service('C:/Users/e007848/Downloads/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.get('https://jqueryui.com/datepicker/')
driver.maximize_window()
driver.switch_to.frame(0)
date_input = driver.find_element(By.ID, 'datepicker')
date_input.click()
future_month = 'March'
year = '2025'
current_month = driver.find_element(By.CLASS_NAME, 'ui-datepicker-month')
current_year = driver.find_element(By.CLASS_NAME, 'ui-datepicker-year')
current_dates = driver.find_elements(By.CLASS_NAME, 'ui-state-default ui-state-active')
#prev_month=driver.find_element(By.CLASS_NAME,'ui-icon ui-icon-circle-triangle-w')
while True:
	next_mon = driver.find_element(By.XPATH, '//*[text()="Next"]/parent::a')
	current_month = driver.find_element(By.CLASS_NAME, 'ui-datepicker-month').text
	current_year = driver.find_element(By.CLASS_NAME, 'ui-datepicker-year').text
	if current_month == future_month and current_year == year:
		dates = driver.find_elements(By.CLASS_NAME, 'ui-state-default')
		for i in dates:
			if '15' in i.text:
				i.click()
				break
		break
	else:
		next_mon.click()
driver.switch_to.default_content()
driver.find_element(By.XPATH,'//a[text()="API documentation"]').click()
time.sleep(5)
