import pandas as pd
import pyodbc

df = pd.read_csv('1_1.txt',sep=" ", header = None)
df.columns = ["First Name","Last Name","Gender","Course","Department","Section"]
print (df)
print(df.iloc[1]['First Name'])
i = 0
# ccc = "insert into table_2 values ('1_1','%s',%s,getdate())" % (df.iloc[i]['mac'],df.iloc[i]['rssi'])
# print(ccc)
while i < len(df):
    #print(type(df.iloc[i]['mac']))
    #ccc = "insert into table_2 values('1_1','" + df.iloc[i]['mac'] + "'," + df.iloc[i]['rssi'] + ",getdate())"
    #print(ccc)
    query = "insert into data_student values ('%s','%s','%s','%s','%s','%s')" % (df.iloc[i]['First Name'], df.iloc[i]['Last Name'], df.iloc[i]['Gender'], df.iloc[i]['Course'], df.iloc[i]['Department'], df.iloc[i]['Section'])
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=COMPUTER\SQLEXPRESS;DATABASE=default; Trusted_Connection=yes;')
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    #print(df.iloc[i]['rssi'])
    i+=1
