import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

serv_obj = Service('C:/Users/e007848/Downloads/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.get('https://admin-demo.nopcommerce.com/login') #Navigate the given url

driver.maximize_window()  #Maximize the window

WebDriverWait(driver,timeout=10).until(EC.presence_of_element_located((By.ID,'Email')))
username_input=driver.find_element(By.ID,'Email')
password_input=driver.find_element(By.ID,'Password')
login_button=driver.find_element(By.TAG_NAME,'button')
if username_input.is_displayed():
    username_input.clear()
    username_input.send_keys('admin@yourstore.com')
    print('Entered username successfully')
    password_input.clear()
    password_input.send_keys('admin')
    print('Password entered successfully')
    login_button.click()
    print('Successfully clicked on the login button')
    WebDriverWait(driver,timeout=15).until(EC.presence_of_element_located((By.LINK_TEXT,'Logout')))
    sliders=driver.find_elements(By.TAG_NAME,'a')
    print(len(sliders))
    slider=driver.find_elements(By.TAG_NAME,'svg')
    print(len(slider))