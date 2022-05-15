import mysql.connector as connector
con = connector.connect(host='localhost', port=3306,
                        user='root', password='Oracal#1', database='pythontest')

print(con)
