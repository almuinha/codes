#------------------------#
# IMPORTANDO BIBLIOTECAS #
#------------------------#

# CALENDÁRIO
import calendar

# TRABALHANDO COM DATA E HORA
from datetime import date

#----------------------------------#
# PARÂMETROS PARA GERAR CALENDÁRIO #
#----------------------------------#

#--------------#
# MESES DO ANO #
#--------------#
meses = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

#-----------------------------------#
# ARMAZENANDO DAT ATUAL EM VARIÁVEL #
#-----------------------------------#
data_atual = date.today()

#-----------#
# ANO ATUAL #
#-----------#
ano_atual = data_atual.year

#-------------------------------------#
# GERANDO CALENDÁRIO PARA O ANO ATUAL #
#-------------------------------------#
for mes in meses:
    cal = calendar.month(ano_atual, mes)
    print('---------------------')
    print(cal);

