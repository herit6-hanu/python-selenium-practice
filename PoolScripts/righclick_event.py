import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service('C:/Users/e007848/Downloads/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.get('https://www.instagram.com/')
driver.maximize_window()
driver.implicitly_wait(10)
ac=ActionChains(driver)
signup_button=driver.find_element(By.LINK_TEXT,'Sign up')
ac.context_click(signup_button).perform()
ac.send_keys(Keys.ARROW_DOWN).perform()
ac.send_keys(Keys.ARROW_DOWN).perform()
ac.send_keys(Keys.ARROW_DOWN).perform()
ac.send_keys(Keys.ARROW_DOWN).perform()
ac.send_keys(Keys.ARROW_DOWN).perform()
ac.send_keys(Keys.ENTER)
time.sleep(10)