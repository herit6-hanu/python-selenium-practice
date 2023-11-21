import sys
import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service

serv_obj = Service('C:/Users/e007848/Downloads/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.get('https://the-internet.herokuapp.com/basic_auth')
driver.maximize_window()


my_wait = WebDriverWait(driver, timeout=10, poll_frequency=2,
                        ignored_exceptions=[NoSuchElementException, ])
time.sleep(2)
driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth')
time.sleep(3)
if driver.page_source.__contains__('Congratulations! You must have the proper credentials.'):
    print('authentication is successfull..')
else:
    sys.stderr.write('authentication is not successfull')
    sys.exit(1)
