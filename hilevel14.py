import requests
from bs4 import BeautifulSoup
import time

textActive = ""

while True:
	response = requests.get("http://gtec-bks.by/index.php")

	bsResponce = BeautifulSoup(response.content,'html.parser')

	soup_find = bsResponce.find('p', {"style":"text-align:left"})

	if textActive != soup_find.text:

		textActive = soup_find.text

		print("Data updated!")

	time.sleep(60*60*3)