import sqlite3
import mysql.connector
import random
import time
import matplotlib.pyplot as plt
import numpy as np

#criar Grafico
def grafico(graficoMySql,graficoSqlite,x,y,titulo,desc):
    resetXY(x,y)
    for i in graficoMySql:
        x.append(i[0])
        y.append(i[1])

    fig, ax = plt.subplots()

    ax.set_ylabel('Tempo')
    ax.set_xlabel('Numero de Registros')
    ax.set_title(f'Comparação entre MySQL e SQlite3 |{desc}')

    xpoints = np.array(x)
    ypoints = np.array(y)
    ax.plot(xpoints, ypoints,color='blue',label='MySQL')

    # grafico sqlite3
    resetXY(x,y)
    for i in graficoSqlite:
        x.append(i[0])
        y.append(i[1])
    xpoints = np.array(x)
    ypoints = np.array(y)
    ax.plot(xpoints, ypoints,color='red',label='SQLite3')
    
    ax.legend()
    plt.savefig(f'{titulo}'+'.png')

# Reseta array dos graficos
def resetXY(x,y):
    x.clear()
    y.clear()
# Select Especializado    
def selectEspecificado(conector):
    # Definir Cursor
    cursor = conector.cursor()

    acao = """
        select year,state,month,number,date from fire;
        """        
    cursor.execute(acao)
    resultado = cursor.fetchall()
    
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

def insert(conector,registro):
    cursor = conector.cursor()

    # Realiza o registro
    cursor.execute(registro)
    
    #Fechar conexoes
    cursor.close()    

# Insert
def insertTest(conector,registros):

    stringRegistros = ''
    for index,i in enumerate(registros):
        try:
            if index != 0:
                stringRegistros += ','
            reg = f"({i[0]},'{i[1]}','{i[2]}',{i[3]},'{i[4]}')"
            stringRegistros += reg
        except:
            pass

    # Definir Cursor
    cursor = conector.cursor()
    query = f'INSERT INTO fire (year,state,month,number,date) VALUES {stringRegistros} ;'
    
    # Realiza o registro
    cursor.execute(query)

    #Fechar conexoes
    cursor.close()    

def avgTest(conector):

    # Definir Cursor
    cursor = conector.cursor()
    query = 'SELECT avg(number) FROM fire;'

    # Realiza o registro
    cursor.execute(query)

    resultado = cursor.fetchall()

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
   
    acao = """
        delete from fire;
        """

    cursor.execute(acao)
    conector.commit()
    cursor.close()  

#Função Main
def main():
    
    iteracoes = 3 # Número de loop interação
    quantidadeRegistros = 10 # Número de registros que será executado

    # Gráfico Select
    graficoMysqlSelect = []
    graficoSqlite3Select = []

    # grafico avg
    graficoAvgMySQL = []
    graficoAvgSQLite = []
    
    # Gráfico Insert
    graficoMysqlInsert = []
    graficoSqlite3Insert = []
    
    # Gráfico Select Especializado
    graficoMysqlSelectEspecializado = []
    graficoSqlite3SelectEspecializado = []

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
    # Teste Select(*)
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
        
    # Teste Avg        
        # teste mysql
        tempoInicialMysql = time.time()
        avgTest(conectorMysql)
        tempoMysql = (time.time() - tempoInicialMysql)
        graficoAvgMySQL.append([quantidadeRegistros,tempoMysql])

        # teste sqlite3
        tempoInicialSqlite3 = time.time()
        avgTest(conectorSqlite3)
        tempoSqlite3 = (time.time() - tempoInicialSqlite3)
        graficoAvgSQLite.append([quantidadeRegistros,tempoSqlite3])

    # Teste Select Especializado
        # teste mysql
        tempoInicialMysql = time.time()
        selectEspecificado(conectorMysql)
        tempoMysql = (time.time() - tempoInicialMysql)
        graficoMysqlSelectEspecializado.append([quantidadeRegistros,tempoMysql])

        # teste sqlite3
        tempoInicialSqlite3 = time.time()
        selectEspecificado(conectorSqlite3)
        tempoSqlite3 = (time.time() - tempoInicialSqlite3)
        graficoSqlite3SelectEspecializado.append([quantidadeRegistros,tempoSqlite3])

        # Incremento do valor de iteração
        quantidadeRegistros *= 10
  
    # Gráfico Select(*)
    x = []
    y = []
    grafico(graficoMysqlSelect,graficoSqlite3Select,x,y,'graficoSelectAll','Select(*)')
    
    # Gráfico Avg
    grafico(graficoAvgMySQL,graficoAvgSQLite,x,y,'graficoAVG','SELECT AVG()')

    # Gráfico Especializado
    grafico(graficoMysqlSelectEspecializado,graficoSqlite3SelectEspecializado,x,y,'graficoSelectEspecializado','SELECT (campos)')
    
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
    
    # teste mysql
    tempoInicialMysql = time.time()
    avgTest(conectorMysql)
    tempoMysql= (time.time() - tempoInicialMysql)
    graficoAvgMySQL.append([quantidadeRegistros,tempoMysql])

    # teste sqlite3
    tempoInicialSqlite3 = time.time()
    avgTest(conectorSqlite3)
    tempoSqlite3 = (time.time() - tempoInicialSqlite3)
    graficoAvgSQLite.append([quantidadeRegistros,tempoSqlite3])

    # testando insert    
    zerarBanco(conectorMysql)
    zerarBanco(conectorSqlite3)
    quantidadeRegistros = 10

    registros = []
    for interacao in range(iteracoes):        
        for i in range(quantidadeRegistros):
            year = genRandomInt()
            state = genRandomString()
            month = genRandomString()
            number = genRandomInt()
            date = genRandomString()
            registros.append([year,state,month,number,date])
            
        # teste mysql
        tempoInicialMysql = time.time()
        insertTest(conectorMysql,registros)
        tempoMysql= (time.time() - tempoInicialMysql)
        graficoMysqlInsert.append([quantidadeRegistros,tempoMysql])

        # teste sqlite3
        tempoInicialSqlite3 = time.time()
        insertTest(conectorSqlite3,registros)
        tempoSqlite3 = (time.time() - tempoInicialSqlite3)
        graficoSqlite3Insert.append([quantidadeRegistros,tempoSqlite3])

        quantidadeRegistros *= 10
    #Gráfico Insert        
    grafico(graficoMysqlInsert,graficoSqlite3Insert,x,y,'graficoInsert','Insert')
    
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

    main()
