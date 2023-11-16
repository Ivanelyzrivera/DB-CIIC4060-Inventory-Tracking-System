from config.dbconfig import pg_config
import psycopg2

class PartDAO:
    def __init__(self):
        connection_url = "host = localhost dbname =%s user=%s password=%s" % (pg_config['dbname'],
         pg_config['user'],
         pg_config['password'])
        print("Connection URL: " + connection_url)
        self.conn = psycopg2.connect(connection_url)
    
    
    def getAllParts(self):
        cursor = self.conn.cursor()
        result = []
        query  = "Select P_ID ,P_Type,P_Color,P_Weight,P_Name,P_Price,P_Manufacturer,S_ID from Part"
        cursor.execute(query)
        for row in cursor:
            result.append(row)
        return result

