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

#------------------------#
#  INICIANDO NAVEGAÇÃO   #
#------------------------#

# importar driver
chromedriver = "C:/LOCAL_DO_ARQUIVO/chromedriver"
capabilities = { 'chromeOptions':  { 'useAutomationExtension': False,
                                     'args': ['--disable-extensions'] }
              }
driver = webdriver.Chrome(chromedriver, desired_capabilities = capabilities)

# acessar o site do provedor de email
# para o Gmail é necessário habilitar na Guia Segurança o acesso a apps menos seguros
driver.get("https://gmail.com.br")

#------------------------------#
# LOGANDO NO PROVEDOR DE EMAIL #
#------------------------------#

login = driver.find_element_by_css_selector('#identifierId')
login.send_keys('seu_email@gmail.com')
driver.find_element_by_css_selector('#identifierNext > span > span').click()

# é necessário utilizar o time.sleep, caso contrário, o código não será executado de maneira correta
time.sleep(4)

senha = driver.find_element_by_css_selector('#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input')
senha.send_keys('sua_senha')
driver.find_element_by_css_selector('#passwordNext > span > span').click()

time.sleep(4)

#-----------------------#
# ESCREVENDO NOVO EMAIL #
#-----------------------#

driver.find_element_by_css_selector('#\:jt > div > div').click()

# destinatário
destinatario = driver.find_element_by_id(':pk')
destinatario.send_keys('email_de_destino')

# assunto
assunto = driver.find_element_by_id(':p2')
assunto.send_keys('Teste Robô Python')

# mensagem
mensagem = driver.find_element_by_css_selector('#\:q7 > br') # o > br indica que o texto de "mensagem" será inserido no espaço em branco (antes da assinatura, caso exista)
mensagem.send_keys('Testando robô em Python para enviar e-mails.')

# enviando
driver.find_element_by_id(':os').click()

