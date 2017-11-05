import os
import pandas as pd
import pyodbc

# Getting the current working directory
directory_in_str = os.getcwd()
for file in os.listdir(directory_in_str+r"\\chandu"):
     filename = os.fsdecode(file)
     #Looping in inner directory
     innerDirectory = directory_in_str + r"\\chandu\\"+filename+r"\\"     
     for file in os.listdir(innerDirectory):
        filename = os.fsdecode(file)
        if filename.endswith(".txt"):
            # Getting the filename
            filename = os.path.join(innerDirectory, filename)
            df = pd.read_csv(filename,sep=" ", header = None)
            df.columns = ["First Name","Last Name","Gender","Course","Department","Section"]        
            i = 0
            while i < len(df):
                # SQL Query to Insert Data
                query = "insert into data_student values ('%s','%s','%s','%s','%s','%s')" % (df.iloc[i]['First Name'], df.iloc[i]['Last Name'], df.iloc[i]['Gender'], df.iloc[i]['Course'], df.iloc[i]['Department'], df.iloc[i]['Section'])        
                # SQL Connection String
                conn = pyodbc.connect('DRIVER={SQL Server};SERVER=COMPUTER\SQLEXPRESS;DATABASE=default; Trusted_Connection=yes;')
                cursor = conn.cursor()
                cursor.execute(query)
                conn.commit()
                i+=1
                conn.close()
              
