# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 16:04:43 2020

@author: manis
"""

import os
import yaml
# Setting the connection
from Connection import Connection

wh = input("Enter Warehouse ")
db = input("Enter Database ")
s = input("Enter Schema ")

conn = Connection.Connect(wh,db,s)

def execute_query(c, query):
    cursor = c.cursor()
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