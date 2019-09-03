# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2
import requests
import pandas as pd
import shutil
import sys
import os

df = pd.read_csv("Players.csv")

print("Read complete")


url = "https://www.foxsports.com"

for i in range(len(df)):
	print(i)
	url_temp = url+df['Url'][i]
	while(True):
		print("Getting page for " + df['Name'][i])
		try:
			page = requests.get(url_temp)
		except requests.exceptions.RequestException as e:  # This is the correct syntax
			print(e)
			continue
		break

	html = page.content
	soup = BeautifulSoup(html,'lxml')
	try:

		Nat = soup.find('img', class_="wisfb_headshotImage wisfb_bioLargeImg")
		
		source = Nat['src'].split('.')
		source[-4] = '2000'
		source[-5] = '2000'

		source = ('.').join(source)
		while(True):
			response = requests.get(source, stream=True)
			break

		with open('Pictures/Raw/'+df['Name'][i]+'.png', 'wb') as out_file:
			shutil.copyfileobj(response.raw, out_file)


		while(True):
			response = requests.get(source, stream=True)
			break

		posi = soup.find('div', class_="wisbb_secondaryInfo")
		posi_span = posi.find('span')
		posi_actual = posi_span.find(text = True).encode('utf-8')
		if(posi_actual not in os.listdir('Pictures/Positions/')):
			os.mkdir('Pictures/Positions/' + posi_actual)
		with open('Pictures/Positions/' + posi_actual + '/' +df['Name'][i]+'.png', 'wb') as out_file:
			shutil.copyfileobj(response.raw, out_file)
		del response

	except:
		print "Unexpected error:", sys.exc_info()[0]
		continue
