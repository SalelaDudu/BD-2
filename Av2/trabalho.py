import sqlite3
import mysql.connector
import random
import time
import matplotlib.pyplot as plt
import numpy as np

# Select All
def selectAll(conector):

    # Definir Cursor
    cursor = conector.cursor()

    # 
    acao = """
        select * from fire;
        """
    # 
    cursor.execute(acao)

    resultado = cursor.fetchall()

    #Fechar conexoes
    cursor.close()    

# Insert
def insert(conector,registro):

    # Definir Cursor
    cursor = conector.cursor()

    # Realiza o registro
    cursor.execute(registro)
    # conector.commit()

    #Fechar conexoes
    cursor.close()    

# Gerador de String
def genRandomString(tamanho=10):
    chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    string = ''
    for i in range(tamanho):
        string += random.choice(chars)
    return string

# Gerador de Inteiro
def genRandomInt(tamanho=100):
    numeros = range(0,tamanho)
    return random.choice(numeros)

# Zera o banco
def zerarBanco(conector):
    cursor = conector.cursor()

    #
    acao = """
        delete from fire;
        """

    # 
    cursor.execute(acao)
    conector.commit()
    cursor.close()  

#Função Main
def main():       

    graficoMysql = []
    graficoSqlite3 = []

    iteracoes = 2
    quantidadeRegistros = 10

    for interacao in range(iteracoes):

        for i in range(quantidadeRegistros):
            
            year = genRandomInt()
            state = genRandomString()
            month = genRandomString()
            number = genRandomInt()
            date = genRandomString()

            query = f'INSERT INTO fire (year,state,month,number,date) VALUES ({year},"{state}","{month}",{number},"{date}");'

            insert(conectorMysql,query)
            insert(conectorSqlite3,query)
            conectorMysql.commit()
            conectorSqlite3.commit()        

        # teste mysql
        tempoInicialMysql = time.time()
        selectAll(conectorMysql)
        tempoMysql= time.time() - tempoInicialMysql
        print(f"\n\nTempo Mysql {quantidadeRegistros} registros: {tempoMysql}")
        graficoMysql.append([quantidadeRegistros,tempoMysql])

        # teste sqlite3
        tempoInicialSqlite3 = time.time()
        selectAll(conectorSqlite3)
        tempoSqlite3 = time.time() - tempoInicialSqlite3
        print(f"Tempo Sqlite3 {quantidadeRegistros} registros: {tempoSqlite3}")
        graficoSqlite3.append([quantidadeRegistros,tempoSqlite3])

        quantidadeRegistros *= 10

    # grafico mysql
    x = []
    y = []
    for i in graficoMysql:
        x.append(i[0])
        y.append(i[1])

    fig, ax = plt.subplots()

    ax.set_ylabel('Tempo')
    ax.set_xlabel('Numero de Registros')
    ax.set_title('Comparação entre MySQL e SQlite3')

    xpoints = np.array(x)
    ypoints = np.array(y)
    ax.plot(xpoints, ypoints,color='blue')

    # grafico sqlite3
    x = []
    y = []
    for i in graficoSqlite3:
        x.append(i[0])
        y.append(i[1])
    xpoints = np.array(x)
    ypoints = np.array(y)
    ax.plot(xpoints, ypoints,color='red')
    print("Gráfico Salvo!")
    plt.savefig('grafico.png')

# Conexões com os bancos
# Banco em MySql
conectorMysql = mysql.connector.connect(    
    host="LocalHost",
    user="root",
    password="root",
    database="fogo"
)   

# Banco em Sql
conectorSqlite3 = sqlite3.connect('fogo.bd')

if __name__ == '__main__':
    zerarBanco(conectorMysql)
    zerarBanco(conectorSqlite3)

    TempoInicialTeste = time.time()

    main()

    conectorMysql.close()
    conectorSqlite3.close()

    # TempoFinalTeste = time.time()

    # TempoTotalTeste = TempoFinalTeste - TempoInicialTeste    

    # TempoTotalTeste = TempoTotalTeste/60

    # print(f"O Tempo Total decorrido foi: {TempoTotalTeste}")