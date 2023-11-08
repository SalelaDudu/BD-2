import sqlite3
import mysql.connector 
import time

# sqlite3Conn = sqlite3.connect('fogo.bd')
MySqlConn = mysql.connector.connect(user='root',password='root',host='localHost',database='forest-fire')

# cursorSql = sqlite3Conn.cursor()

cursorMysql = MySqlConn.cursor()

select = """select * from fire;"""

# cursorSql.execute(select)

# for i in cursorSql:
#    cursorMysql.execute(f"""insert into fire(year,state,month,number,date) values('{i[0]}','{i[1]}','{i[2]}',{i[3]},'{i[4]}');""")
#     # print(i[0],i[1],i[2],i[3],i[4])

n = time.time()

cursorMysql.execute(select)

print = (time.time() - n)


# cursorSql.close()

cursorMysql.close()

# sqlite3Conn.commit()
# MySqlConn.commit()

# sqlite3Conn.close()
MySqlConn.close()
