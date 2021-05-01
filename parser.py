# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import json
import string

URL = "https://www.weblancer.net/jobs/?page="

headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7",
}


num_of_page = 10


for i in range(num_of_page):
	url = URL + str(i + 1)
	r = requests.get(url, headers=headers) 
	soup = BeautifulSoup(r.text, "html.parser")
	vacancies = soup.find_all("a", {"class": "text-bold show_visited"})



	for v in vacancies:
		# print(v.text)	
		# print(, end="\n\n")
		# URL + v.get("href")
		data = dict.fromkeys(v.text, URL + v.get("href"))

	with open("vacancies.json", "w", encoding='utf-8') as write_file:
		json.dump(data, write_file)
 
 

