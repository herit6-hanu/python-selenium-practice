import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service('C:/Users/e007848/Downloads/chromedriver-win64/chromedriver.exe')
driver=webdriver.Chrome(service=serv_obj)
driver.get('https://google.com')
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea').send_keys('Elon Musk')
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="APjFqb"]').clear()
driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea').send_keys('Elon Musk')
driver.find_element(By.XPATH,'//*[@id="APjFqb"]').send_keys(Keys.ENTER)
time.sleep(3)
driver.get('https://www.facebook.com/')
time.sleep(2)
driver.find_element(By.XPATH,'//input[starts-with(@id,"em")]').send_keys('9100412870')
driver.find_element(By.XPATH,'//input[contains(@id,"pass")]').send_keys('Herit6@143')
driver.find_element(By.XPATH,'//button').click()
time.sleep(10)
