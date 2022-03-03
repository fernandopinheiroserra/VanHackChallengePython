import re
import requests
from bs4 import BeautifulSoup

# your task is to write a function to search a mock bookstore website 
# (Books to Scape) and determine if a title is listed in the store's 
# online inventory.
#    In stock   
#    instock availability

#fonts https://www.youtube.com/watch?v=XVv6mJpFOb0&ab_channel=freeCodeCamp.org


html_text = requests.get('http://books.toscrape.com/').text
soup = BeautifulSoup(html_text, 'lxml')

#product
product = soup.find('article', class_='product_pod')

#title
product_title = product.find('h3')
title = product_title.find('a')
tproduct = "Title: {}".format(title.get("title"))
#availability
product_available = product.find('p', class_='instock availability')
aproduct = product_available.text.strip()


print(f'Título: {tproduct} , Disponibilidade: {aproduct}')




