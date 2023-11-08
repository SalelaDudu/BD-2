import pymysql # Biblioteca para fazer interacao com BD
import time

# Conexao com BD
banco = pymysql.connect(    
    host="LocalHost",
    user="root",
    passwd="root",
    database="forest-fire"
)

# Definir Cursor
cursor = banco.cursor()

 # Definir os valores que serão registrados no banco
acao = """
   select * from fire;
    """

# Realiza o registro
n = time.time()
cursor.execute(acao)
banco.commit()
h = time.time() - n
print(f"tempo: {h}")

#Fechar conexoes
cursor.close()    
banco.close()
