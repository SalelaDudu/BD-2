from dependencias import *

if __name__ == '__main__':
    zerarBanco(conectorMysql)
    zerarBanco(conectorSqlite3)
    
    # potência de n, valor de n
    # t = time.time()
    # popularBanco(2,10)
    # tf = time.time()

    main()
    print("Feito!")