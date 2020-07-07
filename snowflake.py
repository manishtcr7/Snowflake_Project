# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 21:21:46 2020

@author: manis
"""

import snowflake.connector

from ConnectionManger import ConnectionManger

#conn = snowflake.connector.connect(user='rpulagala', password='Welcome@123', account='telus.east-us-2.azure', database='DEMO_DB',schema='PUBLIC',warehouse='PROCESS_WH')
conn = ConnectionManger.Connect()
# warehouse=config.warehouse,
#                            database=config.database, schema=config.schema)

def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    cursor.close()


try:
    sql = 'drop table Complaint'
    cursor = conn.cursor()
    cursor.execute(sql)
    for c in cursor:
        print(c)
        
except Exception as e:
    print(e)