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

#------------------------#
#  INICIANDO NAVEGAÇÃO   #
#------------------------#

#importar driver
chromedriver = "C:/LOCAL_DO_ARQUIVO_EM_SEU_COMPUTADOR/chromedriver"
capabilities = { 'chromeOptions':  { 'useAutomationExtension': False,
                                     'args': ['--disable-extensions'] }
               }
driver = webdriver.Chrome(chromedriver, desired_capabilities = capabilities)

# acessar o site desejado
driver.get("https://twitter.com")

#-----------------------------------------#
# LOGANDO NO TWITTER COM UMA CONTA VÁLIDA #
#-----------------------------------------#

# clicando no botão de Log in
driver.find_element_by_css_selector('#doc > div > div.StaticLoggedOutHomePage-content > div.StaticLoggedOutHomePage-cell.StaticLoggedOutHomePage-utilityBlock > div.StaticLoggedOutHomePage-signupBlock > div.StaticLoggedOutHomePage-noSignupForm > div > a.js-nav.EdgeButton.EdgeButton--medium.EdgeButton--secondary.StaticLoggedOutHomePage-buttonLogin').click()
time.sleep(3)

# inserindo phone, email, username
login = driver.find_element_by_css_selector('#page-container > div > div.signin-wrapper > form > fieldset > div:nth-child(2) > input')
login.send_keys('nome_de_usuario')
time.sleep(4)

# inserindo password
senha = driver.find_element_by_css_selector('#page-container > div > div.signin-wrapper > form > fieldset > div:nth-child(3) > input')
senha.send_keys('sua_senha')

# desmarcar checkbox "remember me"
# por padrão este checkbox vem marcado; caso não seja o primeiro acesso, pode já estar desmarcado
#driver.find_element_by_css_selector('#page-container > div > div.signin-wrapper > form > div.clearfix > div > label > input[type=checkbox]').click()

# clicando no botão de Log in
driver.find_element_by_css_selector('#page-container > div > div.signin-wrapper > form > div.clearfix > button').click()

time.sleep(4)

#----------------------#
#  INICIANDO PESQUISA  #
#----------------------#

# pesquisar por 'oi_oficial'
pesquisar = driver.find_element_by_css_selector('#react-root > div > div > div > main > div > div > div > div.css-1dbjc4n.r-aqfbo4.r-zso239.r-1jocfgc > div > div.css-1dbjc4n.r-gtdqiz.r-1jocfgc > div > div > div > div.css-1dbjc4n.r-1awozwy.r-aqfbo4.r-14lw9ot.r-18u37iz.r-1h3ijdo.r-15d164r.r-1vsu8ta.r-1xcajam.r-ipm5af.r-1jocfgc.r-136ojw6 > div > div > div > form > div.css-1dbjc4n.r-1wbh5a2 > div > div > div.css-901oao.r-hkyrab.r-6koalj.r-16y2uox.r-1qd0xha.r-a023e6.r-16dba41.r-ad9z0x.r-bcqeeo.r-qvutc0 > input')
pesquisar.send_keys('palavra_chave_a_ser_pesquisada')
pyautogui.press("enter")

