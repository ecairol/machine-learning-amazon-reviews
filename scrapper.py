# author: Esteban Cairol - ecairol
# Scraper that receives an Amazon Customer Reviews URL asand writes a txt file per review
# Labels are generated depending on the rating: 0 Negative (1 or 2 stars) - 1 Neutral (3 stars) - 2 Positive (4 or 5 stars)

import os
import requests
import sys
import hashlib
import time
from bs4 import BeautifulSoup

def scrapUrl(url):
	htmlPage = requests.get(url)
	soup = BeautifulSoup(htmlPage.content, 'html.parser')

	try:
		reviewsWrapper = soup.find('div', {'class':'reviews'})
		reviews = reviewsWrapper.find_all(True, {'class':['review']})
	except Exception, e:
		newurl = raw_input('\nURL not supported. Please enter another URL: ')
		scrapUrl(newurl)

	stored = 0
	for review in reviews:
		try:
			stars = int(review.find('i', {'class':'review-rating'}).get_text()[0])
			if stars >= 4:
				label = 2 # Positive
			elif stars <=2:
				label = 0 # Negative
			else:
				label = 1 # Neutral
			
			title = review.find('a', {'class':'review-title'}).get_text()
			text = review.find('span', {'class':'review-text'}).get_text()

			# File
			file_name = "{}_{}.txt".format(label,hashlib.md5(text).hexdigest())
			file_content = "{}\n{}".format(title,text)

			# Delete file if exists
			try:
			    os.remove(file_name)
			except OSError:
			    pass

			# Create file
			text_file = open(os.path.join('data', file_name) ,'w')
			text_file.write(file_content)
			text_file.close()
			stored += 1

			# print label,"\n",title, text, "\n"
		
		except Exception, e:
			print e

	print "\n{} out of {} saved".format(stored,len(reviews))

	newurl = raw_input('\nWant to add another URL? Paste it here: ')
	scrapUrl(newurl)


# url = 'http://www.amazon.com/Acer-Chromebook-11-6-Inch-CB3-111-C670-Celeron/product-reviews/B00MMLV7VQ/ref=cm_cr_dp_see_all_summary?ie=UTF8&showViewpoints=1&sortBy=byRankDescending' 
url = raw_input('Enter an Amazon Customer Reviews URL: ')
scrapUrl(url)


