from config.dbconfig import pg_config
import psycopg2

class WarehouseDAO:
    def __init__(self):
        connection_url = "host = localhost dbname =%s user=%s password=%s" % (pg_config['dbname'],
         pg_config['user'],
         pg_config['password'])
        print("Connection URL: " + connection_url)
        self.conn = psycopg2.connect(connection_url)
    
    
    def getAllWarehouses(self):
        cursor = self.conn.cursor()
        result = []
        query  = "Select W_ID,W_Name,W_Address,W_City From Warehouse"
        cursor.execute(query)
        for row in cursor:
            result.append(row)
        return result
    
    

