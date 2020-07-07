import snowflake.connector
class Connection:
    def Connect(wh, db, s):
        con = snowflake.connector.connect(
            user='rpulagala',
            password='Welcome@123',
            account='telus.east-us-2.azure',
            warehouse=wh,
            database=db,
            schema=s)
        return(con)


