from queue import Empty
import re
import requests
import sys
from bs4 import BeautifulSoup

# your task is to write a function to search a mock bookstore website 
# (Books to Scape) and determine if a title is listed in the store's 
# online inventory.
#    In stock   
#    instock availability

#fonts https://www.youtube.com/watch?v=XVv6mJpFOb0&ab_channel=freeCodeCamp.org

print('Welcome to BookSearch!')
print('Type here the title of the book: ')
book_search = input('>')
print(f'searching for {book_search}...')

html_text = requests.get('http://books.toscrape.com/').text
soup = BeautifulSoup(html_text, 'lxml')

#product
products = soup.find_all('article', class_='product_pod')
book_list = []

for product in products:
    #availability
    product_available = product.find('p', class_='instock availability')
    aproduct = product_available.text.strip()
    #title
    product_title = product.find('h3')
    title = product_title.find('a')
    tproduct = "{}".format(title.get("title"))
    book_list.append(f'Title: {tproduct} , Availability: {aproduct}')  
 
matches = []
for match in book_list:
    if book_search in match:
        matches.append(match) 

#show results       


