import requests as requests
url='http://www.deadlinkcity.com/error-page.asp?e=400'
res=requests.head(url)
if res.status_code>=400:
	print('It is broken link')
else:
	print('The status code of the current link', res.status_code)