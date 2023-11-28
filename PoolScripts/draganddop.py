import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service('C:/Users/e007848/Downloads/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
driver.maximize_window()
ac = ActionChains(driver)
for i in range(1,8):
	ac.drag_and_drop(source=driver.find_element(By.ID,'box'+str(i)+''),target=driver.find_element(By.ID,'box10'+str(i)+'')).perform()
	time.sleep(1)
time.sleep(3)