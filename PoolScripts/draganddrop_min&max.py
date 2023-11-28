import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service('C:/Users/e007848/Downloads/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.get('https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/')
driver.maximize_window()
ac = ActionChains(driver)
min_slider=driver.find_element(By.XPATH,'//*[@id="slider-range"]/span[1]')
max_slider=driver.find_element(By.XPATH,'//*[@id="slider-range"]/span[2]')
print(min_slider.location,max_slider.location)
ac.drag_and_drop_by_offset(min_slider,xoffset=100,yoffset=0).perform()
ac.drag_and_drop_by_offset(max_slider,xoffset=-150,yoffset=0).perform()
print(min_slider.location,max_slider.location)
driver.close()