import sqlite3

banco = sqlite3.connect("fogo.bd")

# Definir Cursor
cursor = banco.cursor()

 # Definir os valores que serão registrados no banco
acao = """
  SELECT count(year) FROM fire;
    """

# Realiza o registro
cursor.execute(acao)

print(cursor.fetchall())


#Fechar conexoes
cursor.close()    
banco.close()