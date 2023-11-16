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
        query = "SELECT P_ID, P_Type, P_Color, P_Weight, P_Name, P_Price, P_Manufacturer, S_ID FROM Part"
        try:
            cursor.execute(query)
            result = []
            for row in cursor:
                result.append(row)
            cursor.close()
            return result
        except Exception as e:
            print("An error occurred: ", e)
        finally:
            cursor.close()

    def getpartbyID(self,pid):
        cursor = self.conn.cursor()
        query = "SELECT P_ID, P_Type, P_Color, P_Weight, P_Name, P_Price, P_Manufacturer, S_ID FROM Part where p_id =%s"
        try:
            cursor.execute(query, (pid,))
            result = cursor.fetchone()
            return result
        except Exception as e:
            print("An error occurred: ", e)
        finally:
            cursor.close()


    def insertPart(self,type,color,weight,name,price,manufacturer,supplierID):
        cursor = self.conn.cursor()
        query = "insert into part(P_Type, P_Color, P_Weight, P_Name,P_Price,P_Manufacturer,S_ID) values (%s, %s, %s, %s, %s, %s, %s) returning P_ID"
        cursor.execute(query, (type, color, weight, name, price, manufacturer, supplierID,))
        P_ID = cursor.fetchone()[0]
        self.conn.commit()
        return P_ID