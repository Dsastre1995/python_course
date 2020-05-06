from bs4 import BeautifulSoup
import requests
from time import sleep
from csv import DictWriter

url = 'http://quotes.toscrape.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

def get_quotes_data():
    print(f'Scraping data...')
    data = list()
    next_page_link = '/page/1'
    while next_page_link:
        response = requests.get(f'{ url }{ next_page_link }')
        sleep(2)
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all(class_ = 'quote')
        for quote in quotes:
            data.append({
                'text': quote.find(class_ = 'text').get_text(),
                'author': quote.find(class_ = 'author').get_text(),
                'bio-info': f'{ url }{ quote.find("a")["href"] }'
            })
        next_page_link = soup.find(class_ = 'next').a['href'] if soup.find(class_ = 'next') else None
    
    return data

def create_csv_quotes(quotes):
    with open('quotes.csv', 'w') as file:
        headers = ['text', 'author', 'bio-info']
        dict_writer = DictWriter(file, fieldnames = headers)
        dict_writer.writeheader()
        for quote in quotes:
            dict_writer.writerow(quote)

quotes = get_quotes_data()
create_csv_quotes(quotes)