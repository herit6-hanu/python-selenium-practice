import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service

serv_obj = Service('C:/Users/e007848/Downloads/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.get('https://the-internet.herokuapp.com/javascript_alerts')
driver.maximize_window()
my_wait = WebDriverWait(driver, timeout=10, poll_frequency=2,
                        ignored_exceptions='[NoSuchElementException, StateElementReferenceException]')
first_alert = driver.find_element(By.XPATH, '//button[text()="Click for JS Alert"]')
second_alert = driver.find_element(By.XPATH, '//button[text()="Click for JS Confirm"]')
third_alert = driver.find_element(By.XPATH, '//button[text()="Click for JS Prompt"]')
first_alert.click()
alert_1 = driver.switch_to.alert
print(alert_1.text)
alert_1.accept()
second_alert.click()
alert_2 = driver.switch_to.alert
print(alert_2.text)
alert_2.dismiss()
third_alert.click()
alert_3 = driver.switch_to.alert
print(alert_3.text)
alert_3.send_keys('Katrina')
alert_3.accept()
res = driver.find_element(By.ID, 'result')
assert res.text == 'You entered: Katrina', 'Entered text in alert is not equal to the result'
time.sleep(2)
driver.quit()
