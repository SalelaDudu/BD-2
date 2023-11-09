import sqlite3
import mysql.connector
import random
import time
import matplotlib.pyplot as plt
import numpy as np

iteracoes = 3 # Número de loop interação
quantidadeRegistros = 10 # Número de registros que será executado

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
    # Gráfico Select
    graficoMysqlSelect = []
    graficoSqlite3Select = []

    # Gráfico Insert
    graficoMysqlInsert = []
    graficoSqlite3Insert = []

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
        tempoMysql= (time.time() - tempoInicialMysql)
        graficoMysqlSelect.append([quantidadeRegistros,tempoMysql])

        # teste sqlite3
        tempoInicialSqlite3 = time.time()
        selectAll(conectorSqlite3)
        tempoSqlite3 = (time.time() - tempoInicialSqlite3)
        graficoSqlite3Select.append([quantidadeRegistros,tempoSqlite3])

        # print do tempo        
        print(f"\n\nempo Mysql {quantidadeRegistros} registros: {tempoMysql}")
        print(f"Tempo Sqlite3 {quantidadeRegistros} registros: {tempoSqlite3}")
        
        # Incremento do valor de iteração
        quantidadeRegistros *= 10

# Gráfico Select    
    # grafico mysql
    x = []
    y = []
    for i in graficoMysqlSelect:
        x.append(i[0])
        y.append(i[1])

    fig, ax = plt.subplots()

    ax.set_ylabel('Tempo')
    ax.set_xlabel('Numero de Registros')
    ax.set_title('Comparação entre MySQL e SQlite3 | Select')

    xpoints = np.array(x)
    ypoints = np.array(y)
    ax.plot(xpoints, ypoints,color='blue')

    # grafico sqlite3
    x = []
    y = []
    for i in graficoSqlite3Select:
        x.append(i[0])
        y.append(i[1])
    xpoints = np.array(x)
    ypoints = np.array(y)
    ax.plot(xpoints, ypoints,color='red')
    plt.savefig('graficoSelect.png')

# Gráfico Insert
    # grafico mysql
    x = []
    y = []
    for i in graficoMysqlInsert:
        x.append(i[0])
        y.append(i[1])

    fig, ax = plt.subplots()

    ax.set_ylabel('Tempo')
    ax.set_xlabel('Numero de Registros')
    ax.set_title('Comparação entre MySQL e SQlite3 | insert')

    xpoints = np.array(x)
    ypoints = np.array(y)
    ax.plot(xpoints, ypoints,color='blue')

    # grafico sqlite3
    x = []
    y = []
    for i in graficoSqlite3Insert:
        x.append(i[0])
        y.append(i[1])
    xpoints = np.array(x)
    ypoints = np.array(y)
    ax.plot(xpoints, ypoints,color='red')
    plt.savefig('graficoInsert.png')

    #Fechar Conexões

    conectorMysql.close()
    conectorSqlite3.close()

# Conexões com os bancos
# Banco em MySql
conectorMysql = mysql.connector.connect(    
    host="LocalHost",
    user="root",
    password="root",
    database="forest-fire"
)   

# Banco em Sql
conectorSqlite3 = sqlite3.connect('fogo.bd')

if __name__ == '__main__':
    zerarBanco(conectorMysql)
    zerarBanco(conectorSqlite3)

    TempoInicialTeste = time.time()

    main()

    TempoFinalTeste = time.time()

    TempoTotalTeste = TempoFinalTeste - TempoInicialTeste    

    TempoTotalTeste = TempoTotalTeste

    print(f"O Tempo Total decorrido foi: {TempoTotalTeste}")