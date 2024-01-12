from bs4 import BeautifulSoup
import urllib.request
import csv
stronawww =  'https://stooq.pl/t/?i=532'
# zapytanie do strony internetowej i zwrocenie wyniku w postaci kodu html oraz przypisanie do zmiennej "obiekt"
obiekt = urllib.request.urlopen(stronawww)
# parsowanie html z uzyciem BeautifulSoup i przypisanie do zmiennej "soup"
soup = BeautifulSoup(obiekt, 'html.parser')

# sprawdzanie czy istnieja dane w tabeli
table = soup.find('table', attrs={'class': 'fth1'})
ilosc_wierszy = table.find_all('tr')
# zliczenie liczby wierszy w tabeli, ale pominiecie pierwszego jako naglowka, wynikiem powinno byc 20
print('Liczba spółek', len(ilosc_wierszy)-1)