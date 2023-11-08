import sqlite3
import pymysql
import random
import time
import matplotlib.pyplot as plt
import numpy as np

def selectAll(conector):

    # Definir Cursor
    cursor = conector.cursor()

    # Definir os valores que serão registrados no banco
    acao = """
        select * from fire;
        """

    # Realiza o registro
    cursor.execute(acao)

    resultado = cursor.fetchall()

    # print(resultado)

    #Fechar conexoes
    cursor.close()    
    #conector.close()

def insert(conector,registro):

    # Definir Cursor
    cursor = conector.cursor()

    # Realiza o registro
    cursor.execute(registro)
    # conector.commit()

    #Fechar conexoes
    cursor.close()    
    #conector.close()

def genRandomString(tamanho=10):
    chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    string = ''
    for i in range(tamanho):
        string += random.choice(chars)
    return string

def genRandomInt(tamanho=100):
    numeros = range(0,tamanho)
    return random.choice(numeros)

def zerarBanco(conector):
    cursor = conector.cursor()

    # Definir os valores que serão registrados no banco
    acao = """
        delete from fire;
        """

    # Realiza o registro
    cursor.execute(acao)
    conector.commit()
    cursor.close()  

def main():       

    graficoMysql = []
    graficoSqlite3 = []

    iteracoes = 100
    quantidadeRegistros = 100

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

        quantidadeRegistros += 100

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
    # plt.savefig('graficoMysql.png')

    # grafico sqlite3
    x = []
    y = []
    for i in graficoSqlite3:
        x.append(i[0])
        y.append(i[1])
    xpoints = np.array(x)
    ypoints = np.array(y)
    ax.plot(xpoints, ypoints,color='red')
    plt.savefig('grafico.png')


conectorMysql = pymysql.connect(    
    host="LocalHost",
    user="root",
    passwd="root",
    database="forest-fire"
)   

conectorSqlite3 = sqlite3.connect('fogo.bd')


if __name__ == '__main__':
    zerarBanco(conectorMysql)
    zerarBanco(conectorSqlite3)

    main()

    conectorMysql.close()
    conectorSqlite3.close()