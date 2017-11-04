import os
# Gets the current working directory
directory_in_str = os.getcwd()
#Looping in outer directory
for file in os.listdir(directory_in_str+r"\\chandu"):
     filename = os.fsdecode(file)
     #Looping in inner directory
     for file in os.listdir(directory_in_str + r"\\chandu\\"+filename):
        filename = os.fsdecode(file)
        if filename.endswith(".txt"):
            print(os.path.join(directory_in_str, filename))
            print(filename)
