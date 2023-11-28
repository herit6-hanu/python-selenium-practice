import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service('C:/Users/e007848/Downloads/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
time.sleep(3)
# scroll the page with the help pf pixels
driver.execute_script(script='window.scrollBy(0,1100)')
current_view=driver.execute_script(script='return window.pageYOffset;')
print(current_view)
time.sleep(1)
# scroll the page with the help of web elements
el=driver.find_element(By.ID,'textarea')
driver.execute_script('arguments[0].scrollIntoView();',el)
time.sleep(1)
 # scroll to the bottom of the page
driver.execute_script('window.scrollBy(0,document.body.scrollHeight)')
current_view=driver.execute_script(script='return window.pageYOffset;')
print(current_view)
driver.close()