import sqlite3
from _sqlite3 import Error

try:
    conn = sqlite3.connect('College.db')
    print(sqlite3.version)
    c = conn.cursor()
    # For executing multiple sripts
    c.executescript(''' CREATE TABLE IF NOT EXISTS STUDENT(
    ID INT PRIMARY KEY      NOT NULL,
    NAME           CHAR(50) NOT NULL,
    DEPT           CHAR(50) NOT NULL,
    COURSE         CHAR(50) NOT NULL
    );

    CREATE TABLE IF NOT EXISTS COMPANY(
   ID INT PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL,
   AGE            INT     NOT NULL,
   ADDRESS        CHAR(50),
   SALARY         REAL
);

    ''')

    c.execute("""   INSERT
    INTO
    COMPANY(ID, NAME, AGE, ADDRESS, SALARY)
    VALUES(5, 'chandu', 24, 'Banglore', 20000.00);

""")
    conn.commit()
    c.execute("SELECT * FROM COMPANY")
    rows = c.fetchall()
    print (rows[1][4],type(rows))
    for row in rows:
        print(row)
    conn.close()
except Error as e:
    print(e)
finally:
    conn.close()

