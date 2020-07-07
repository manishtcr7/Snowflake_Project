#f = open("C:/Users/manis/Desktop/CreateTable.txt", "r")
#x = f.read()

import os
import yaml
# Setting the connection
from ConnectionManger import ConnectionManger

conn = ConnectionManger.Connect()

def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    cursor.close()


# Retreiving subdirectories of the current working directory.
subdirs = [X[0] for X in os.walk('C:/Users/manis/Desktop/SQL')]
os.chdir('C:/Users/manis/Desktop/SQL')

# Looping through every folder and appending the data to their respective lists.
for s in subdirs:
    os.chdir(s)
    for file in os.listdir():
        if file.endswith(".sql")==True:
            f = open(file, "r")
            x = f.read()
#            print(x)
            
            try:
                sql = x
                execute_query(conn,sql)
                
            except Exception as e:
                print(e)
                




