#------------------------#
# IMPORTANDO BIBLIOTECAS #
#------------------------#

# GERAR NROS PSEUDOALEATÓRIOS
import random

#----------------------------------#
# CARACTERES PARA COMPOR AS SENHAS #
#----------------------------------#

minusculas = "abcdefghijklmnopqrstuvwxyz"
maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"
simbolos = "[]{}()*;/,._-"

#-----------------------------#
# PARÂMETROS PARA GERAR SENHA #
#-----------------------------#

caracteres_em_geral = minusculas + maiusculas + numeros + simbolos
tamanho_da_senha = 10
senha = "".join(random.sample(caracteres_em_geral, tamanho_da_senha))

#-------------------------#
# EXIBINDO A SENHA GERADA #
#-------------------------#

print(senha)

