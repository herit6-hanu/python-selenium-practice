import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service('C:/Users/e007848/Downloads/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.get('https://www.dummyticket.com/dummy-ticket-for-visa-application/')
driver.implicitly_wait(10)
driver.maximize_window()
ac=ActionChains(driver)
dob_input = driver.find_element(By.ID,
                                'dob')
ac.move_to_element(dob_input)
time.sleep(1)
dob_input.click()
year_dropdown = Select(driver.find_element(By.CLASS_NAME,
                                           'ui-datepicker-year'))

year_dropdown.select_by_visible_text('2000')
month_dropdown = Select(driver.find_element(By.CLASS_NAME,
                                            'ui-datepicker-month'))
month_dropdown.select_by_visible_text('May')
dates = driver.find_elements(By.CLASS_NAME,
                             'ui-state-default')
for date in dates:
	if date.text == '5':
		date.click()
		break
time.sleep(3)
driver.quit()
