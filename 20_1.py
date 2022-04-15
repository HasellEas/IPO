from bs4 import BeautifulSoup
import requests

urls = ["http://gtec-bks.by/","https://5element.by/","https://www.kufar.by/listings"]

is_ok = [False]*len(urls)

for url in urls:
	url_html = requests.get(url)
	if str(url_html) == "<Response [200]>":
		print(BeautifulSoup(url_html.content,'html.parser'))
		is_ok[urls.index(url)] = True
	else:
		print("Error with open "+url+": "+str(url_html))

for __ in urls:
	print("\n\n\nStatus "+__+": "+str(is_ok[urls.index(__)]))