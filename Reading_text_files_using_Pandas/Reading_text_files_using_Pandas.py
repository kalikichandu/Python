import pandas as pd

# Include the Separator character in 'sep' argument
df = pd.read_csv('1_1.txt',sep=" ", header = None)
# Define the columns for your data
df.columns = ["First Name","Last Name","Gender","Course","Department","Section"]
# Prints the Data Frame
print (df)
# Printing the particular values
print(df.iloc[1]['First Name'])
