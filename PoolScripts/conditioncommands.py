import locators
from selenium.webdriver.chrome.service import Service


serv_obj = Service('C:/Users/e007848/Downloads/chromedriver-win64/chromedriver.exe')

# driver=webdriver.Chrome(service=serv_obj)
# driver.get('https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F')
# driver.maximize_window()  # Maximize the window
locators.login()
search_box = locators.driver.find_element('css selector', 'input[placeholder="Search"]')
print(search_box.is_displayed())
print(search_box.is_enabled())
# browser commands
locators.driver.quit()
