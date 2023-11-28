import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service('C:/Users/e007848/Downloads/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3')
driver.maximize_window()
ac = ActionChains(driver)
driver.switch_to.frame('iframeResult')

field1 = driver.find_element(By.ID,
                             'field1')
print(field1.get_attribute('tagName'))
time.sleep(2)
field1.clear()
field2 = driver.find_element(By.ID,
                             'field2')
field1.send_keys('Welcome Hanumantha Reddy')
button=driver.find_element(By.XPATH,'//button[text()="Copy Text"]')
ac.double_click(button).perform()
time.sleep(5)
if field1.get_attribute('value') == field2.get_attribute('value'):
	print('Values in field 1 & field 2 are equal')
else:
	print(field1.get_attribute('value'),field2.get_attribute('value'))
	print('Values in field 1 & field 2 are not equal')
