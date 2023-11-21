import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
serv_obj = Service('C:/Users/e007848/Downloads/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.get('https://www.hyrtutorials.com/p/frames-practice.html')
driver.maximize_window()
name_input=driver.find_element(By.XPATH,'//input[@id="name"]')
name_input.send_keys('Hanumantha Reddy')
time.sleep(5)
frame_1=driver.switch_to.frame('frm1')
dropdown=Select(driver.find_element(By.XPATH,'//select[@id="selectnav1"]'))
option=dropdown.options
for opt in option:
	print(opt.text)
dropdown.select_by_visible_text('Tutorials')
time.sleep(2)
print('pass')
driver.switch_to.default_content()
name_input.clear()
time.sleep(5)
driver.quit()
