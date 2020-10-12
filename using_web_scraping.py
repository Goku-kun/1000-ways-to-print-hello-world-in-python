import lxml
import bs4
import requests

website = requests.get('https://en.wikipedia.org/wiki/%22Hello,_World!%22_program')
website = bs4.BeautifulSoup(website.text, "lxml")

paras = website.select('p')

print(paras[0].getText()[3:16])
