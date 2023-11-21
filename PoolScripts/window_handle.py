import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
serv_obj = Service('C:/Users/e007848/Downloads/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.get('https://nxtgenaiacademy.com/multiplewindows/')
driver.maximize_window()
driver.find_element(By.XPATH,'//button[normalize-space()="New Browser Tab"]').click()
time.sleep(2)
driver.find_element(By.LINK_TEXT,'New Browser Tab Link').click()
tabs=driver.window_handles
for tab in tabs:
	driver.switch_to.window(tab)
	print(f'The current title of the tab is {driver.title}')
	time.sleep(2)
	driver.close()
