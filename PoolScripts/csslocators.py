import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service('C:/Users/e007848/Downloads/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
driver.maximize_window()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, 'input.oxd-input').send_keys('Admin')#  css locator ==>tag.classname(withoutspaces) tagname is optional
driver.find_element(By.CSS_SELECTOR, 'input[name=password]').send_keys('admin123')#css locator ==>tag[att=value] tagname is optional
driver.find_element(By.CSS_SELECTOR, 'button').click()
time.sleep(5)