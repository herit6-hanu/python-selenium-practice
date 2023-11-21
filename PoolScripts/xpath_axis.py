import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

serv_obj = Service('C:/Users/e007848/Downloads/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.get('https://google.com')
driver.maximize_window()

# finding the search element using the parent xpath axis
driver.find_element(By.XPATH, '//*[@name="q"]/parent::*/textarea').send_keys('Elon Musk')
webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
# finding the text with elon musk using starts-with
elements = driver.find_elements(By.XPATH, '//*[starts-with(text(),"Elon Musk")]')
for el in elements:
	if el.text != '':
		print(el.text)
time.sleep(5)
