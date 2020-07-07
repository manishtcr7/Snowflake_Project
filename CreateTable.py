# Setting the connection
from ConnectionManger import ConnectionManger

conn = ConnectionManger.Connect()

def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    cursor.close()

try:
    sql = 'CREATE TABLE IF NOT EXISTS Customer (CustomerName String, CustomerID String, CustomerAge Number, PhoneNumber String)'
    cursor = conn.cursor()
    cursor.execute(sql)
    for c in cursor:
        print(c)
        
except Exception as e:
    print(e)