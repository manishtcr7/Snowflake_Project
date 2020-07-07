# Setting the connection
from ConnectionManger import ConnectionManger
from snowflake.connector import DictCursor

conn = ConnectionManger.Connect()

def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    cursor.close()

try:
    csv_file = 'C:/Users/manis/Desktop/Cust.csv'

    sql = 'put file://{0} @{1} auto_compress = true'.format(csv_file, 'LoadCSV')
    execute_query(conn, sql)
    
    sql = "copy into Demo_DB.public.Customer from @LoadCSV/Cust.csv.gz FILE_FORMAT=(TYPE=csv field_delimiter=',' skip_header=1)"
    execute_query(conn, sql)
    
    
    sql = 'Select * from Customer'
    cursor = conn.cursor(DictCursor)
    cursor.execute(sql)
    for c in cursor:
        print(c)
       
except Exception as e:
    print(e)