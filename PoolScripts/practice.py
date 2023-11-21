from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

options=Options()
options.add_argument('headless')
serv_obj=Service('C:/Users/e007848/Downloads/chromedriver-win64/chromedriver.exe')
driver=webdriver.Chrome(service=serv_obj,options=options)
driver.get('https://google.com')
driver.quit()
print('Success')