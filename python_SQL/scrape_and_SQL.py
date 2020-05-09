from bs4 import BeautifulSoup
import sqlite3
import requests

URL = 'http://books.toscrape.com/'
book_posible_ratings = { 'Zero': 0, 'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5 }

def get_book_title(book):
    return book.find('h3').find('a')['title']

def get_book_price(book):
    price = book.select('.price_color')[0].get_text()
    return float(price.replace('£', " ").replace('Â', " "))

def get_book_rating(book):
    paragraph = book.select('.star-rating')[0]
    rating = paragraph.get_attribute_list('class')[-1]
    return book_posible_ratings.get(rating)

def save_books(books):
    coon = sqlite3.connect('books.db')
    cursor = coon.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS book (title TEXT, price FLOAT, raring INTEGER);")
    cursor.executemany('INSERT INTO book VALUES (?, ?, ?)', books)
    coon.commit()
    coon.close();

def scrape_books(url):
    books_data = list()
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.find_all(class_ = 'product_pod')

    for book in books:
        book_data = (get_book_title(book), get_book_price(book), get_book_rating(book))
        books_data.append(book_data)

    return books_data



books = scrape_books(URL)
save_books(books)