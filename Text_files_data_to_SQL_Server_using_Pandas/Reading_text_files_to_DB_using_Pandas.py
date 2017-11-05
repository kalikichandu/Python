import os
import pandas as pd
import pyodbc

directory_in_str = os.getcwd()
for file in os.listdir(directory_in_str+r"\\chandu"):
     filename = os.fsdecode(file)
     #Looping in inner directory
     innerDirectory = directory_in_str + r"\\chandu\\"+filename+r"\\"     
     for file in os.listdir(innerDirectory):
        filename = os.fsdecode(file)
        if filename.endswith(".txt"):
            filename = os.path.join(innerDirectory, filename)
            df = pd.read_csv(filename,sep=" ", header = None)
            df.columns = ["First Name","Last Name","Gender","Course","Department","Section"]
            print (df)
            print(df.iloc[1]['First Name'])
            i = 0
            while i < len(df):
                query = "insert into data_student values ('%s','%s','%s','%s','%s','%s')" % (df.iloc[i]['First Name'], df.iloc[i]['Last Name'], df.iloc[i]['Gender'], df.iloc[i]['Course'], df.iloc[i]['Department'], df.iloc[i]['Section'])
                print(query)
                conn = pyodbc.connect('DRIVER={SQL Server};SERVER=COMPUTER\SQLEXPRESS;DATABASE=default; Trusted_Connection=yes;')
                cursor = conn.cursor()
                cursor.execute(query)
                conn.commit()
                i+=1
                conn.close()
              
