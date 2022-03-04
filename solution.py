import requests
from bs4 import BeautifulSoup
from tkinter import *

# your task is to write a function to search a mock bookstore website 
# (Books to Scape) and determine if a title is listed in the store's 
# online inventory.
#    In stock   
#    instock availability

#fonts https://www.youtube.com/watch?v=XVv6mJpFOb0&ab_channel=freeCodeCamp.org

def bookSearch():
    book_search = entry.get()

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
        book_list.append(f'Title: {tproduct}')  
    
    matches = []
    for match in book_list:
        if book_search in match:
            matches.append(match) 
    return matches
   

#looking Good!
root = Tk()

root.geometry("800x600")

print('Type here the title of the book: ')
root.title('Welcome to BookSearch!')

prompt = Label(root, text='Type the title (or a part of it) for the search: ', padx=10, pady=20)
prompt.pack()

entry = Entry(root, width=100)
entry.pack(pady=30)

def btClick():        
    input_words = entry.get()
    for item in bookSearch():
        listbox.insert(0, item)
    listbox.pack(expand=YES, fill=BOTH, padx=10, pady=10)    

okButton = Button(root, text='Search!', padx=20, pady=10, command=btClick)
okButton.pack()

prompt = Label(root, text='The following itens are In Stock: ', padx=10, pady=10)
prompt.pack()

listbox = Listbox(root)


root.mainloop()



