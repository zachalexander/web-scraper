from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import json
from apscheduler.schedulers.blocking import BlockingScheduler

import logging
logging.basicConfig()


#function to scrape data for Fox News

def data_print():

	#beautifulSoup notation to scrape Fox News
	r = requests.get("http://www.foxnews.com/politics.html")
	soup = BeautifulSoup(r.content, "html.parser")
	headline = soup.find_all("h1")
	fox_pic = soup.find('img')['src']
	fox_title = headline[1].a.get_text()
	fox_url = headline[1].find("a")["href"]


	#beautifulSoup notation to scrape Breitbart News
	r2 = requests.get("http://www.breitbart.com/big-government/")
	soup2 = BeautifulSoup(r2.content, "html.parser")
	bb_headline = soup2.find_all("div", class_ = "col8 top-article")
		
	for x in bb_headline:
		bb_alm_url = x.find("h2", class_ = "title")
		bb_url = bb_alm_url.find("a")["href"]
		bb_title = bb_alm_url.find("a")["title"]
		
	for y in bb_headline:
		bb_pic = y.find("img")["src"]
		
	
	#beautifulSoup notation to scrape NPR
	r2 = requests.get("http://www.npr.org/sections/politics/")
	soup2 = BeautifulSoup(r2.content, "html.parser")
	npr_headline = soup2.find_all("div", class_ = "item-image")
	npr_pic = npr_headline[0].find("img")["src"]
	npr_url = npr_headline[0].find("a")["href"]
	npr_title = npr_headline[0].find("img")["alt"]	
	
	#creating json library
	data = {}
	data["News Pull"] = [{"title":[], "photo": [], "url": []}]
	
	#pulling this into data.json
	with open("data.json", "w") as writeJSON:
		data['title'] = fox_title
		data['pic'] = fox_pic
		data['url'] = fox_url
		data['title2'] = bb_title
		data['pic2'] = bb_pic
		data['url2'] = bb_url
		data['title3'] = npr_title
		data['pic3'] = npr_pic
		data['url3'] = npr_url
		json.dump(data, writeJSON)	
		#print data
		

#pulling from Fox News and Breitbart every hour
scheduler = BlockingScheduler()
scheduler.add_job(data_print, 'interval', seconds=1)
scheduler.start()




	


















