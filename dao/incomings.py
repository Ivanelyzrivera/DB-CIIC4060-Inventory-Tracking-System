from config.dbconfig import pg_config
import psycopg2

class IncomingDAO:
    def __init__(self):
        connection_url = "host = ec2-107-22-101-0.compute-1.amazonaws.com dbname =%s user=%s password=%s" % (pg_config['dbname'],
         pg_config['user'],
         pg_config['password'])
        print("Connection URL: " + connection_url)
        self.conn = psycopg2.connect(connection_url)
    
    
    def getAllIncomings(self):
        cursor = self.conn.cursor()
        query = "SELECT I_ID,  T_ID FROM Incoming;"
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
    
    def getincomingbyID(self,iid):
        cursor = self.conn.cursor()
        query = "SELECT I_ID, T_ID FROM Incoming where i_id =%s"
        try:
            cursor.execute(query, (iid,))
            result = cursor.fetchone()
            return result
        except Exception as e:
            print("An error occurred: ", e)
        finally:
            cursor.close()

    def insertIncoming(self,transactionID):
        cursor = self.conn.cursor()
        query = "insert into incoming(T_ID) values (%s) returning I_ID"
        cursor.execute(query, (transactionID,))
        I_ID = cursor.fetchone()[0]
        self.conn.commit()
        return I_ID
    
    def deleteById(self, iid):
        cursor = self.conn.cursor()
        query = " delete FROM Incoming where i_id =%s"
        cursor.execute(query, (iid,))
        count = cursor.rowcount
        self.conn.commit()
        return count
    
    def putByID(self,iid,transactionID):
        cursor = self.conn.cursor()
        query = "update incoming set T_ID = %s where i_id = %s;"
        cursor.execute(query, (transactionID, iid,))
        count = cursor.rowcount
        self.conn.commit()
        return count
    
    def findRackToPlace(self,partID,warehouseID):
        cursor = self.conn.cursor()
        query = "SELECT P_ID, W_ID, R_ID, R_Stock, R_Capacity FROM Part natural inner join Rack where p_id =%s and w_id=%s;"
        try:
            cursor.execute(query, (partID, warehouseID,))
            result = []
            for row in cursor:
                result.append(row)
            cursor.close()
            return result
        except Exception as e:
            print("An error occurred: ", e)
        finally:
            cursor.close()
        
        count = cursor.rowcount
        self.conn.commit()
        return count
    
