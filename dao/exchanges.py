from config.dbconfig import pg_config
import psycopg2

class ExchangeDAO:
    def __init__(self):
        connection_url = "host = localhost dbname =%s user=%s password=%s" % (pg_config['dbname'],
         pg_config['user'],
         pg_config['password'])
        print("Connection URL: " + connection_url)
        self.conn = psycopg2.connect(connection_url)
    
    
    def getAllExchanges(self):
        cursor = self.conn.cursor()
        query = "SELECT E_ID, E_Reason, W_ID_Destination, U_ID_Destination, T_ID FROM Exchange;"
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

    def getexchangebyID(self,eid):
        cursor = self.conn.cursor()
        query = "SELECT E_ID, E_Reason, W_ID_Destination, U_ID_Destination, T_ID FROM Exchange where e_id =%s"
        try:
            cursor.execute(query, (eid,))
            result = cursor.fetchone()
            return result
        except Exception as e:
            print("An error occurred: ", e)
        finally:
            cursor.close()
    
    def insertExchange(self,reason,warehouseIDdestination,userIDdestination,transactionID):
        cursor = self.conn.cursor()
        query = "insert into exchange(E_Reason, W_ID_Destination, U_ID_Destination, T_ID) values (%s, %s, %s, %s) returning E_ID"
        cursor.execute(query, (reason,warehouseIDdestination,userIDdestination,transactionID,))
        E_ID = cursor.fetchone()[0]
        self.conn.commit()
        return E_ID
    
    def deleteById(self, eid):
        cursor = self.conn.cursor()
        query = " delete FROM Exchange where e_id =%s"
        cursor.execute(query, (eid,))
        count = cursor.rowcount
        self.conn.commit()
        return count
    
    def putByID(self,eid ,reason,warehouseIDdestination,userIDdestination,transactionID):
        cursor = self.conn.cursor()
        query = "update part set E_Reason = %s, W_ID_Destination =%s, U_ID_Destination = %s, T_ID = %s where e_id = %s;"
        cursor.execute(query, (reason,warehouseIDdestination,userIDdestination,transactionID, eid,))
        count = cursor.rowcount
        self.conn.commit()
        return count