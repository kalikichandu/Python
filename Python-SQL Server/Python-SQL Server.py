import pyodbc
#Connection String for SQL Server through windows authentication
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=COMPUTER\SQLEXPRESS;DATABASE=default; Trusted_Connection=yes;')
cursor = conn.cursor()
cursor.execute("SELECT * FROM data_student")
for row in cursor.fetchall():
    print (row)
conn.close()
