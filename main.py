from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

url = 'https://books.toscrape.com/'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}

page = requests.get(url, headers = headers)

soup = BeautifulSoup(page.text, 'html.parser')
print()
'''print('String: ' + soup.find_all('a')[54].string)
print('Title: ' + soup.find_all('a')[54].get('title'))
'''
titlesoup = soup.find_all('a')
'''list comprehension'''
titlelist = [title.get('title') for i, title in enumerate(titlesoup) if i>= 54 and i % 2 == 0]



pricesoup = soup.find_all('p', class_='price_color')

pricelist = [price.string.replace('Â£', '') for price in pricesoup]


dictDF = {'Title': titlelist,
          'Price': pricelist}

print(dictDF)

bookDF = pd.DataFrame(dictDF)

print(bookDF)