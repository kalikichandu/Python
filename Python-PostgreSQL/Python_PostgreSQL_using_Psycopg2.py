import psycopg2
from psycopg2 import DatabaseError

try:
    conn = psycopg2.connect("dbname='mylocaldb' user='postgres' host='localhost' password='pranusha'")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS COMPANY(
   ID INT PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL,
   AGE            INT     NOT NULL,
   ADDRESS        CHAR(50),
   SALARY         REAL
);
""")
    conn.commit()
    cur.execute("""SELECT * FROM COMPANY
    """)
    rows = cur.fetchall()
    print(rows, type(rows))
    print(rows[0][1], type(rows))
    conn.close()
except DatabaseError as ex:
    print(ex)
finally:
    conn.close()
