from config.dbconfig import pg_config
import psycopg2

class SupplierDAO:
    def __init__(self):
        connection_url = "host = localhost dbname =%s user=%s password=%s" % (pg_config['dbname'],
         pg_config['user'],
         pg_config['password'])
        print("Connection URL: " + connection_url)
        self.conn = psycopg2.connect(connection_url)
    
    
    def getAllSuppliers(self):
        cursor = self.conn.cursor()
        result = []
        query  = "SELECT S_ID,S_Name,S_Address,S_Email,S_PhoneNumber,S_City from Supplier"
        cursor.execute(query)
        for row in cursor:
            result.append(row)
        return result

