import os
import selectors
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import pandas as pd
from scrapy import Selector

data_danych = '04-01-2024'

driver = webdriver.Chrome()
driver.get('https://www.gpw.pl/archiwum-notowan')

pop = driver.find_element(By.XPATH,'//*[@id="onetrust-button-group"]/div').click()

dropdown = Select(driver.find_element(By.XPATH, '//*[@id="selectType"]'))
dropdown.select_by_value("10")


data= driver.find_element(By.XPATH,'//*[@id="date"]').send_keys(data_danych)
plik = driver.find_element(By.XPATH, '//*[@id="archiwum-notowan-search"]/div[5]/a').click()

time.sleep(2)

# data_danych1 = datetime.strptime(data_danych, '%m-%d-%Y').strftime('%Y-%d-%m')
# print(data_danych1)
# plik = f"_{data_danych1}_akcje"
# sciezka = os.path.join('C:\\Users\\Użytkownik\\Downloads', f'{plik}.xls')
# df = pd.read_excel(sciezka, usecols=['Data', 'Nazwa', 'Kurs zamknięcia', 'Zmiana'])
# df = df.loc[df['Nazwa'].isin (['PEKAO','PKOBP'])]
# df.rename(columns={'Data': 'DATA_DANYCH', 'Nazwa': 'NAZWA', 'Kurs zamknięcia': 'CENA'}, inplace=True)
# df.to_excel('C:\\Users\\Użytkownik\\Downloads\\wyniki.xlsx')



# driver1=webdriver.Chrome()
# driver1.get('https://stooq.pl/q/i/?s=wig_banki&o=10&i')
# time.sleep(4)
# pop = driver1.find_element(By.XPATH,'/html/body/div/div[2]/div[1]/div[2]/div[2]/button[1]/p').click()
# # time.sleep(4)
# #
# # tabela = driver1.find_element(By.XPATH,'//*[@id="fth1"]')
# tabela = driver1.find_element(By.XPATH, '//*[@id="fth1"]')
# time.sleep(4)
# tabela=pd.read_html(tabela.get_attribute('outerHTML'))


# tabela2=tabela1
# tabela2=tabela[0]
# tabela2=tabela1.loc[tabela1['Nazwa'].isin (['PEKAO','PKOBP'])]
# tabela1