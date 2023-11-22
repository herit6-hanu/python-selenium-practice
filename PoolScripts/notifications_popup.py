import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

serv_obj = Service('C:/Users/e007848/Downloads/chromedriver-win64/chromedriver.exe')
opt = Options()
# opt.add_experimental_option("prefs", {"profile.managed_default_content_settings.geolocation": 2})
opt.add_argument('--disable-notification')
driver = webdriver.Chrome(service=serv_obj)
driver.get('https://whatmylocation.com/')
driver.maximize_window()
time.sleep(5)
