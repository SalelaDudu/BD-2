import mysql.connector as my_conn
import random

# Banco em MySql
banco = my_conn.connect(    
    host="LocalHost",
    user="root",
    password="root",
    database="av3_d"
)

insercoes = (100 * 1000) - 1

strings = []
ints = []
query = f"INSERT INTO cliente(nome,cpf) VALUES('Jorge João',129101)"

# Gerador de String
def geraString(tamanho = 20):
    chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    string = ''
    for i in range(tamanho):
        string += random.choice(chars)
    return string
# Gerador de Inteiro
def geraInt(tamanho = 20000):
    numeros = range(100,tamanho)
    return random.choice(numeros)
# Insert
def insert(banco,query):
    cursor = banco.cursor()
    cursor.execute(query)
    banco.commit()
    cursor.close()
# Select    
def select(banco,cursor):
    cursor = 'select * from cliente;'
    banco.execute(cursor)
    cursor.fetchall()
          
for i in range(insercoes):
    strings.append(geraString())
    ints.append(geraInt())

for i in range(insercoes):
    s = f",('{strings[i]}',{ints[i]})"
    query+= s

query += ';'

insert(banco,query)

# Fechar Conexão
banco.close()