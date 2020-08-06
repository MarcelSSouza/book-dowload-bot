import smtplib,ssl
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from os import *
from time import *
from smtplib import *
from re import sub
from decimal import Decimal

livro=input("Digite o nome do livro desejado: ")
url="http://www.b-ok.cc/"
options = webdriver.ChromeOptions();
driver=webdriver.Chrome(options=options)
driver.get(url)
sleep(10)



search_bar= driver.find_element_by_xpath('//*[@id="searchFieldx"]')
search_bar.send_keys(livro)
sleep(3)
search_button= driver.find_element_by_xpath('//*[@id="searchForm"]/div[1]/div/div[2]/div/button')
search_button.click()
sleep(10)
first_result= driver.find_element_by_xpath('//*[@id="searchResultBox"]/div[2]/div/table/tbody/tr/td[2]/table/tbody/tr[1]/td/h3/a')
first_result.click()
sleep(5)
dowload_button= driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/div/div/div/div[2]/div[2]/div[1]/div[1]/div/a')
dowload_button.click()
print('Parabéns o livro {} está sendo baixado. Você o encontrará na sua pasta de Dowloads em alguns segundos! '.format(livro))
sleep(100)

