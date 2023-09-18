'''
Autor: Eduardo Santos
Data: 18/09/2023 
Ultima alteracao: 18/09/2023 
'''

import pymysql # Biblioteca para fazer interacao com BD


# Conexao com BD
banco = pymysql.connect(    
    host="localhost",
    user="root",
    passwd="root",
    database="sakila"
)

# Definir Cursor
cursor = banco.cursor()

# Definir qual consulta sera feita (consulta a)
consulta = """
  select actor_id,first_name, last_name from actor where actor_id in 
  (select actor_id from film_actor where film_id in (select film_id from film where title = "TRAP GUYS"));
"""

# Realiza a consulta
cursor.execute(consulta)

# Exibir os dados no terminal
print("\nRESULTADO:") # Formatacao visual

print("-"*35) # Formatacao visual
for (actor_id,first_name, last_name) in cursor:
    print(f"{actor_id}| {first_name} {last_name}")

print("-"*35) # Formatacao visual

#Fechar conexoes
cursor.close()    
banco.close()

'''
 Fim do codigo até 18/09/2023
 modificado por : Eduardo Santos
 '''