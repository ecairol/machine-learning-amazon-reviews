import requests
from bs4 import BeautifulSoup

url = raw_input('Enter the an Amazon Review URL: ')

htmlPage = requests.get(url)
soup = BeautifulSoup(htmlPage.content, 'html.parser')


reviewsWrapper = soup.find('div', {'class':'reviews'})
reviews = reviewsWrapper.find_all('span', {'class':'review-text'})

for review in reviews:
    print "\n",review.get_text()

print "\nProcessed ", len(reviews), " reviews"