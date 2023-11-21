import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
serv_obj=Service('C:/Users/e007848/Downloads/chromedriver-win64/chromedriver.exe')
opt=Options()
#opt.add_argument('headless')
driver=webdriver.Chrome(service=serv_obj,options=opt)
driver.implicitly_wait(10)
driver.get('https://in.search.yahoo.com/')
driver.maximize_window()
driver.find_element(By.XPATH,'//*[@placeholder="Search the web"]').send_keys('Python')
webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
driver.find_element(By.XPATH,'//a[text()="Welcome to Python.org"]').click()
driver.find_element(By.XPATH,'//*[@class="button button--dark button--small button--primary"]').click()
time.sleep(50)
print('success')