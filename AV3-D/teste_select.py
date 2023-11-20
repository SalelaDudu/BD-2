import mysql.connector
import time

# Banco em MySql
bd = mysql.connector.connect(    
    host="LocalHost",
    user="root",
    password="root",
    database="av3_d"
)
# Select
def select(banco):
    cursor = banco.cursor()
    query = 'select nome,cpf from cliente;'
    cursor.execute(query)

t0 = time.time()
select(bd)
tf = time.time()
tt = tf - t0
print(f"Tempo decorrido: {tt}")


# Fechar Conexão

bd.close()    