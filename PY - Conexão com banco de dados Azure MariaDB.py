#------------------------------------#
# IMPORTANDO BIBLIOTECAS NECESSÁRIAS #
#------------------------------------#

import pymysql
import mysql.connector as mariadb


#----------------------------------------#
# ABRINDO A CONEXÃO COM O BANCO DE DADOS #
#----------------------------------------#

cnx = mariadb.connect(
                      user="user_name"
                     ,password='user_password'
                     ,host="server_name"
                     ,port=3306
                     ,database='database_name'
                     )

# instancia um objeto cursor utilizando o método cursor

cursor = cnx.cursor()

#---------------------#
# GERANDO COMANDO SQL #
#---------------------#

sql = """SELECT * FROM products;"""

cursor.execute(sql)

#--------------------------------#
# EXIBINDO RESULTADO DA CONSULTA #
#--------------------------------#

rows = cursor.fetchall()

for row in rows:
    print(row)

#------------------#
# FECHANDO CONEXÃO #
#------------------#

cnx.close()

