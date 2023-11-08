import sqlite3

banco = sqlite3.connect('fogo.bd')

# Definir Cursor
cursor = banco.cursor()

 # Definir os valores que serão registrados no banco
acao = """
   INSERT INTO fire(year,state,month,number,date) VALUES (12,"aaaaa","aaaa",12,"asdadsad");
    """


# Realiza o registro
cursor.execute(acao)

#Fechar conexoes
cursor.close()    
banco.close()