import os
import requests
from bs4 import BeautifulSoup
URL='https://github.com/Goku-kun/1000-ways-to-print-hello-world-in-python'

def get_all_URL(URL):
	urls = []
	reqs = requests.get(URL)
	soup = BeautifulSoup(reqs.text, 'html.parser')
	for link in soup.find_all('a'):
		urls.append(link.get('href'))
	return urls
	
	
def Filter_pyfiles(urls):
	filtered=[]
	start='/Goku-kun/1000-ways-to-print-hello-world-in-python/blob/master/'
	end='.py'
	for url in urls:
		if url.startswith(start) and url.endswith(end):
			filtered.append(url)
	return filtered
	
def get_textfile(number,urls):
	number%=(len(urls)-1)#if ur lucky number is not bounded 
	url="https://raw.githubusercontent.com"+urls[number]
	newurl=''.join(url.split('/blob'))
	output=os.popen('wget \''+newurl+'\''+' -O helloworld'+str(number)+'.py').read()
	return 'helloworld'+str(number)+'.py'	
	
def print_output(name):
	output=os.popen('python '+name).read()
	print(output)
def main():
	url_list=get_all_URL(URL)
	filtered=Filter_pyfiles(url_list)
	number=int(input("enter your lucky number:"))
	name=get_textfile(number,filtered)	
	print_output(name)
	os.remove(name)
main()
