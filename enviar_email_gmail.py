import time # lib para utilizar o time.sleep

# lib selenium para utilizar os atributos do chromedriver (acesso ao navegador Chrome)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

#importar driver
chromedriver = "LOCAL_DO_ARQUIVO/chromedriver"
capabilities = { 'chromeOptions':  { 'useAutomationExtension': False,
                                     'args': ['--disable-extensions'] }
              }
driver = webdriver.Chrome(chromedriver, desired_capabilities = capabilities)

# acessar o site do provedor de email
driver.get("https://gmail.com.br")

# para o Gmail é necessário habilitar na Guia Segurança o acesso a apps menos seguros

# logando no provedor de email
login = driver.find_element_by_css_selector('#identifierId')
login.send_keys('seu_email@gmail.com')
driver.find_element_by_css_selector('#identifierNext > span > span').click()
# é necessário utilizar o time.sleep, caso contrário, o código não será executado de maneira correta e vai travar nos pontos onde deveria ter o time.sleep
time.sleep(4)
senha = driver.find_element_by_css_selector('#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input')
senha.send_keys('sua_senha')
driver.find_element_by_css_selector('#passwordNext > span > span').click()
time.sleep(4)

# escrevendo novo email
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
