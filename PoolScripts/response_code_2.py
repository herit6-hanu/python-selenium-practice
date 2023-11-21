import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
serv_obj=Service('C:/Users/e007848/Downloads/chromedriver-win64/chromedriver.exe')
opt=Options()
opt.add_argument('headless')
driver=webdriver.Chrome(service=serv_obj,options=opt)
driver.get('http://www.deadlinkcity.com/')
driver.maximize_window()
elements=driver.find_elements(By.XPATH,'//a[contains(text(),"here") or contains(text(),"Errorcode")]' )
links=[]
for el in elements:
	link=el.get_attribute('href')
	links.append(link)
for i in range(len(links)):
	res=requests.head(links[i])
	res_code=res.status_code
	if res_code>=400:
		print(f'The response code of the link {links[i]} with text {elements[i].text} ==> {res_code} , so we consider it as broken file or there is no source on the hyper-reference')
	else:
		print(f'The response code of the links {links[i]} with text {elements[i].text} ==> {res_code} , so we consider it as internal or external link')
driver.quit()
	