import requests
from bs4 import BeautifulSoup

URL = "https://www.weblancer.net/jobs/?page="

headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7",
}

# print(r, end="\n\n")

num_of_page = 10

for i in range(num_of_page):
	url = URL + str(i + 1)
	r = requests.get(url, headers=headers) 
	soup = BeautifulSoup(r.text, "html.parser")
	vacances = soup.find_all("a", {"class": "text-bold show_visited"})



	for v in vacances:
		print(v.text)	
		print(URL + v.get("href"), end="\n\n")
 
 

