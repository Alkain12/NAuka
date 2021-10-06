import requests
from bs4 import BeautifulSoup
import pandas as pd

# start_url = "https://www.gala-group.com"
start_url = input("Podaj adres strony - ")
download_html = requests.get(start_url)

soup = BeautifulSoup(download_html.text)
with open('downloaded.html', 'w', encoding="utf-8") as file:
    file.write(soup.prettify())

