import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException,InvalidElementStateException
from selenium.webdriver.common.by import By
opt=Options()
serv_obj=Service('C:/Users/e007848/Downloads/chromedriver-win64/chromedriver.exe')
driver=webdriver.Chrome(service=serv_obj)
driver.get('https://www.youtube.com/')
driver.maximize_window()
mywait=WebDriverWait(driver,timeout=10,ignored_exceptions=['NoSuchElementException'])
ac=webdriver.ActionChains(driver)
search_input=mywait.until(EC.presence_of_element_located((By.XPATH,'//input[@id="search"]')))
search_input.send_keys('Hungry Cheetah teaser')
search_input.submit()
teaser_link=mywait.until(EC.presence_of_element_located((By.XPATH,'//*[text()="Hungry Cheetah - OG Glimpse | Pawan Kalyan | Sujeeth | Thaman S | DVV Danayya"]')))
teaser_link.click()
time.sleep(2)
ac.send_keys('f').perform()
time.sleep(110)
print('He is th real hungry cheetah 🧡🆔♊♒㊗🉐🚱🚳🚷✅✳🚰🚻2️⃣1️⃣8️⃣▶↩↕🟢🟡▪🐱‍👤🤳😃😃🤳😎🎶😢🐱‍👤🎶🤦‍♂️')