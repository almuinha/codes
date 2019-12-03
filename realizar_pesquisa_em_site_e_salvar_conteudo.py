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

# BeautifulSoup para extrair texto
from bs4 import BeautifulSoup

#------------------------#
#  INICIANDO NAVEGAÇÃO   #
#------------------------#

#importar driver
chromedriver = "C:/LOCAL_DO_ARQUIVO/chromedriver"
capabilities = { 'chromeOptions':  { 'useAutomationExtension': False,
                                     'args': ['--disable-extensions'] }
               }
driver = webdriver.Chrome(chromedriver, desired_capabilities = capabilities)

# acessar o site do provedor de email
driver.get("https://docs.microsoft.com/pt-br/")

#-------------------#
# REALIZAR PESQUISA #
#-------------------#

# clicar no campo Pesquisar
driver.find_element_by_css_selector('#form-expander > span.icon > span').click()

# digitar termo a ser pesquisado
pesquisar = driver.find_element_by_id('site-search-input')
pesquisar.send_keys('CAST e CONVERT')

time.sleep(3)

# tecla Enter para realizar pesquisa
pyautogui.press("enter")

time.sleep(4)

# clicar no link da pesquisa que contém as informações desejadas
driver.find_element_by_css_selector('#main > div.searchResults.has-reading-max-width > ol > li:nth-child(1) > h2 > a').click()

time.sleep(5)

#----------------------------------------------------#
# ARMAZENAR INFORMAÇÕES ENCONTRADAS EM ARQUIVO EXCEL #
#----------------------------------------------------#

# criando arquivo
wb = xlsxwriter.Workbook('C:/LOCAL_DO_ARQUIVO/Dados_da_pesquisa.xlsx')
ws = wb.add_worksheet('Dados')

#-----------#
# CABEÇALHO #
#-----------#

# formatação do cabeçalho
wb_format = wb.add_format({'bold': 1, 'align': 'center'})

# mapeando colunas do cabeçalho (que neste caso, são quatro)
cab_col_1 = driver.find_element_by_css_selector('#main > div:nth-child(20) > table > thead > tr > th:nth-child(1) > span:nth-child(1)')
soup_cab_col_1 = BeautifulSoup(cab_col_1.text, 'html.parser')

cab_col_2 = driver.find_element_by_css_selector('#main > div:nth-child(20) > table > thead > tr > th:nth-child(2) > span:nth-child(1)')
soup_cab_col_2 = BeautifulSoup(cab_col_2.text, 'html.parser')

cab_col_3 = driver.find_element_by_css_selector('#main > div:nth-child(20) > table > thead > tr > th:nth-child(3) > span:nth-child(1)')
soup_cab_col_3 = BeautifulSoup(cab_col_3.text, 'html.parser')

cab_col_4 = driver.find_element_by_css_selector('#main > div:nth-child(20) > table > thead > tr > th:nth-child(4) > span:nth-child(1)')
soup_cab_col_4 = BeautifulSoup(cab_col_4.text, 'html.parser')

# escrevendo cabeçalho no arquivo
ws.write('A1', str(soup_cab_col_1), wb_format)
ws.write('B1', str(soup_cab_col_2), wb_format)
ws.write('C1', str(soup_cab_col_3), wb_format)
ws.write('D1', str(soup_cab_col_4), wb_format)

#-------#
# DADOS #
#-------#

# mapeando dados
tabela = driver.find_element_by_css_selector('#main > div:nth-child(20) > table > tbody')
linhas_da_tabela = len(driver.find_elements_by_css_selector('#main > div:nth-child(20) > table > tbody > tr'))

# iniciando contador das linhas da tabela e da planilha
i = 1 # linha da tabela (tr)
r = 2 # linha da planilha (após o cabeçalho, inicia na linha 2)

# enquanto a qtd de linhas de dados encontradas for menor que a qtd total de linhas da tabela, faça:
while i < linhas_da_tabela + 1:
    
    #------------------#
    # MAPEANDO COLUNAS #
    #------------------#
    
    #------------------------------#
    # COLUNA 1 - (td:nth-child(1)) #
    #------------------------------#
    # armazenando valor em variável
    tab_col_1 = driver.find_element_by_css_selector('#main > div:nth-child(20) > table > tbody > tr:nth-child({})'.format(i) + ' > td:nth-child(1)')
    # extraindo texto da variável
    soup_tab_col_1 = BeautifulSoup(tab_col_1.text, 'html.parser')
    # escrevendo valor no arquivo
    ws.write('A' + str(r), str(soup_tab_col_1))
    
    #------------------------------#
    # COLUNA 2 - (td:nth-child(2)) #
    #------------------------------#
    # armazenando valor em variável
    tab_col_2 = driver.find_element_by_css_selector('#main > div:nth-child(20) > table > tbody > tr:nth-child({})'.format(i) + ' > td:nth-child(2)')
    # extraindo texto da variável
    soup_tab_col_2 = BeautifulSoup(tab_col_2.text, 'html.parser')
    # escrevendo valor no arquivo
    ws.write('B' + str(r), str(soup_tab_col_2))
    
    #-------------------------------#
    # COLUNA 3 - (td:nth-child(3))  #
    #-------------------------------#
    # armazenando valor em variável
    tab_col_3 = driver.find_element_by_css_selector('#main > div:nth-child(20) > table > tbody > tr:nth-child({})'.format(i) + ' > td:nth-child(3)')
    # extraindo texto da variável
    soup_tab_col_3 = BeautifulSoup(tab_col_3.text, 'html.parser')
    # escrevendo valor no arquivo
    ws.write('C' + str(r), str(soup_tab_col_3))
    
    #------------------------------#
    # COLUNA 4 - (td:nth-child(4)) #
    #------------------------------#
    # armazenando valor em variável
    tab_col_4 = driver.find_element_by_css_selector('#main > div:nth-child(20) > table > tbody > tr:nth-child({})'.format(i) + ' > td:nth-child(4)')
    # extraindo texto da variável
    soup_tab_col_4 = BeautifulSoup(tab_col_4.text, 'html.parser')
    # escrevendo valor no arquivo
    ws.write('D' + str(r), str(soup_tab_col_4))
    
    #-------------------------#
    # INCREMENTANDO VARIÁVEIS #
    #-------------------------#
    i = i + 1 # linha da tabela (tr)
    r = r + 1 # linha da planilha
    
# salvando e fechando arquivo
wb.close()
