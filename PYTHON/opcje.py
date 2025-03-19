import os
import selectors
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import pandas as pd
from scrapy import Selector


driver = webdriver.Chrome()
driver.get('https://www.gpw.pl/instrumenty-pochodne')

pop = driver.find_element(By.XPATH,'//*[@id="nj"]').click()
time.sleep(35)


# dropdown = Select(driver.find_element(By.XPATH, '//*[@id="selectType"]'))
# dropdown.select_by_value("10")
#
#
# data= driver.find_element(By.XPATH,'//*[@id="date"]').send_keys(data_danych)
# plik = driver.find_element(By.XPATH, '//*[@id="archiwum-notowan-search"]/div[5]/a').click()
#
