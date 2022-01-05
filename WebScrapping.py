import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0'}
#User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0
page = requests.get("https://www.google.com/search?client=firefox-b-d&q=dolar+hoje", headers=headers)

#print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')


#span class="DFlfde SwHCTb"


valor_dolar = soup.find_all("span", class_="DFlfde SwHCTb")[0]

print(valor_dolar)
print(valor_dolar.text)
print(valor_dolar['data-value'])