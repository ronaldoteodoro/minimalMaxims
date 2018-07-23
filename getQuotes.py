from bs4 import BeautifulSoup
import requests

def get_quote():
        response = requests.get('https://minimalmaxims.com/')
        search_html = response.text
        soup = BeautifulSoup(search_html, 'html.parser')
        text = soup.find(class_="quotable-quote")
        rawQuote = text.find('p')
        quote = rawQuote.text.strip()
        print quote
get_quote()