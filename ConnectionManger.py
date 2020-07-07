import snowflake.connector
class ConnectionManger:
    def Connect():
        con = snowflake.connector.connect(
            user='rpulagala',
            password='Welcome@123',
            account='telus.east-us-2.azure',
            warehouse='PROCESS_WH',
            database='DEMO_DB',
            schema='PUBLIC')
        return(con)


