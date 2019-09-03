# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2
import requests
import pandas as pd

url1 = "https://www.foxsports.com/nfl/players?teamId=0&season=2019&position=0&page="
url2 = "&country=0&grouping=0&weightclass=0"

A=[]
B=[]

for i in range(140):
	url = url1 + str(i + 1) + url2
	page = requests.get(url)
	html = page.content
	soup = BeautifulSoup(html,'lxml')
	right_table = soup.findAll('div', class_='wisbb_playerContainer')
	
	flag = 0
	for a in right_table:
		row = a.find("a")
		row1 = row.find('span')
		A.append(row1.find(text = True).encode('utf-8'))
		B.append(row["href"])
		print("Done for " + row1.find(text = True))

	print('Working on page ' + str(i))

df = pd.DataFrame({
	"Name" 	: A,
	"Url"	: B
	})

df.to_csv("Players.csv", index = False)