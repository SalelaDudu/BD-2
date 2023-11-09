import sqlite3
import time

banco = sqlite3.connect("fogo.bd")

# Definir Cursor
cursor = banco.cursor()

 # Definir os valores que serão registrados no banco
acao = """
  SELECT count(year) FROM fire;
    """

# Realiza o registro
Tempoinicial = time.time()

cursor.execute(acao)

TempoFinal= time.time() - Tempoinicial

print("Concluído!")
print(f"Tempo decorrido: {TempoFinal}")

#Fechar conexoes
cursor.close()    
banco.close()