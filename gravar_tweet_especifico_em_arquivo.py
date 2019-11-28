#------------------------#
# IMPORTANDO BIBLIOTECAS #
#------------------------#

# time.sleep
import time

# atributos do chromedriver (acesso ao navegador Chrome)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

# controlar movimentos do mouse
import pyautogui

# manipular arquivos Excel
import xlsxwriter
import pandas as pd
from pandas import ExcelWriter

# extrair texto
from bs4 import BeautifulSoup

#------------------------#
#  INICIANDO NAVEGAÇÃO   #
#------------------------#

#importar driver
chromedriver = "LOCAL_DO_ARQUIVO/chromedriver"
capabilities = { 'chromeOptions':  { 'useAutomationExtension': False,
                                     'args': ['--disable-extensions'] }
               }
driver = webdriver.Chrome(chromedriver, desired_capabilities = capabilities)

# acessar o site do provedor de email
driver.get("https://twitter.com")

#-----------------------------------------#
# LOGANDO NO TWITTER COM UMA CONTA VÁLIDA #
#-----------------------------------------#

# clicando no botão de Log in
driver.find_element_by_css_selector('#doc > div > div.StaticLoggedOutHomePage-content > div.StaticLoggedOutHomePage-cell.StaticLoggedOutHomePage-utilityBlock > div.StaticLoggedOutHomePage-signupBlock > div.StaticLoggedOutHomePage-noSignupForm > div > a.js-nav.EdgeButton.EdgeButton--medium.EdgeButton--secondary.StaticLoggedOutHomePage-buttonLogin').click()
time.sleep(3)

# inserindo phone, email, username
login = driver.find_element_by_css_selector('#page-container > div > div.signin-wrapper > form > fieldset > div:nth-child(2) > input')
login.send_keys('seu_login')
time.sleep(4)

# inserindo password
senha = driver.find_element_by_css_selector('#page-container > div > div.signin-wrapper > form > fieldset > div:nth-child(3) > input')
senha.send_keys('sua_senha')

# desmarcar checkbox "remember me"
# por padrão este checkbox vem marcado; caso não seja o primeiro acesso, pode já estar desmarcado
driver.find_element_by_css_selector('#page-container > div > div.signin-wrapper > form > div.clearfix > div > label > input[type=checkbox]').click()

# clicando no botão de Log in
driver.find_element_by_css_selector('#page-container > div > div.signin-wrapper > form > div.clearfix > button').click()

time.sleep(8)

#----------------------#
#  INICIANDO PESQUISA  #
#----------------------#

# pesquisar por palavra-chave, usuário, etc
pesquisar = driver.find_element_by_css_selector('#react-root > div > div > div > main > div > div > div > div.css-1dbjc4n.r-aqfbo4.r-zso239.r-1jocfgc > div > div.css-1dbjc4n.r-gtdqiz.r-1jocfgc > div > div > div > div.css-1dbjc4n.r-1awozwy.r-aqfbo4.r-14lw9ot.r-18u37iz.r-1h3ijdo.r-15d164r.r-1vsu8ta.r-1xcajam.r-ipm5af.r-1jocfgc.r-136ojw6 > div > div > div > form > div.css-1dbjc4n.r-1wbh5a2 > div > div > div.css-901oao.r-hkyrab.r-6koalj.r-16y2uox.r-1qd0xha.r-a023e6.r-16dba41.r-ad9z0x.r-bcqeeo.r-qvutc0 > input')
pesquisar.send_keys('palavra_chave_ou_usuario_a_ser_pesquisado')
pyautogui.press("enter")

time.sleep(3)

#----------------------------------------------#
# SALVANDO ITENS DA PESQUISA EM PLANILHA EXCEL #
#----------------------------------------------#

# criando pasta de trabalho com planilha nomeada de "Tweets"
wb = xlsxwriter.Workbook('LOCAL_DO_ARQUIVO/Coleta_de_tweets.xlsx')
ws = wb.add_worksheet('Tweets')

# formatação para o cabeçalho
wb_format = wb.add_format({'bold': 1, 'align': 'center'})

# escrevendo títulos nas colunas
ws.write('A1', 'Data', wb_format)
ws.write('B1', 'Tweet', wb_format)
ws.write('C1', 'Comentários', wb_format)
ws.write('D1', 'Retweets', wb_format)
ws.write('E1', 'Curtidas', wb_format)

time.sleep(4)

# armazenando valores em variáveis
data_tweet = driver.find_element_by_css_selector('#react-root > div > div > div > main > div > div > div > div > div > div:nth-child(2) > div > div > section > div > div > div > div:nth-child(6) > div > article > div > div:nth-child(2) > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-5f2r5o.r-1mi0q7o > div:nth-child(1) > div.css-1dbjc4n.r-1d09ksm.r-18u37iz.r-1wbh5a2 > a')
soup_data = BeautifulSoup(data_tweet.text, 'html.parser')

tweet = driver.find_element_by_css_selector('#react-root > div > div > div > main > div > div > div > div > div > div:nth-child(2) > div > div > section > div > div > div > div:nth-child(6) > div > article > div > div:nth-child(2) > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-5f2r5o.r-1mi0q7o > div.css-901oao.r-hkyrab.r-1qd0xha.r-a023e6.r-16dba41.r-ad9z0x.r-bcqeeo.r-bnwqim.r-qvutc0')
soup_tweet = BeautifulSoup(tweet.text, 'html.parser')

comentarios = driver.find_element_by_css_selector('#react-root > div > div > div > main > div > div > div > div > div > div:nth-child(2) > div > div > section > div > div > div > div:nth-child(6) > div > article > div > div:nth-child(2) > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-5f2r5o.r-1mi0q7o > div.css-1dbjc4n.r-18u37iz.r-1wtj0ep.r-156q2ks.r-1mdbhws > div:nth-child(1) > div > div > div.css-1dbjc4n.r-xoduu5.r-1udh08x > span')
soup_comentarios = BeautifulSoup(comentarios.text, 'html.parser')

retweets = driver.find_element_by_css_selector('#react-root > div > div > div > main > div > div > div > div > div > div:nth-child(2) > div > div > section > div > div > div > div:nth-child(6) > div > article > div > div:nth-child(2) > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-5f2r5o.r-1mi0q7o > div.css-1dbjc4n.r-18u37iz.r-1wtj0ep.r-156q2ks.r-1mdbhws > div:nth-child(2) > div > div > div.css-1dbjc4n.r-xoduu5.r-1udh08x > span')
soup_retweets = BeautifulSoup(retweets.text, 'html.parser')

curtidas = driver.find_element_by_css_selector('#react-root > div > div > div > main > div > div > div > div > div > div:nth-child(2) > div > div > section > div > div > div > div:nth-child(6) > div > article > div > div:nth-child(2) > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-5f2r5o.r-1mi0q7o > div.css-1dbjc4n.r-18u37iz.r-1wtj0ep.r-156q2ks.r-1mdbhws > div:nth-child(3) > div > div > div.css-1dbjc4n.r-xoduu5.r-1udh08x > span')
soup_curtidas = BeautifulSoup(curtidas.text, 'html.parser')

# escrevendo valores na planilha
ws.write('A2', str(soup_data))
ws.write('B2', str(soup_tweet))
ws.write('C2', str(soup_comentarios))
ws.write('D2', str(soup_retweets))
ws.write('E2', str(soup_curtidas))

# salvando e fechando arquivo
wb.close()
