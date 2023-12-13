from config.dbconfig import pg_config
import psycopg2

class OutgoingDAO:
    
    def __init__(self):
        connection_url = "host = ec2-107-22-101-0.compute-1.amazonaws.com dbname =%s user=%s password=%s" % (pg_config['dbname'],
         pg_config['user'],
         pg_config['password'])
        print("Connection URL: " + connection_url)
        self.conn = psycopg2.connect(connection_url)
    
    
    def getAllOutgoings(self):
        cursor = self.conn.cursor()
        query = "SELECT O_ID, O_SellPrice, O_Customer, O_Destination, T_ID FROM Outgoing"
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

    def getoutgoingbyID(self,oid):
        cursor = self.conn.cursor()
        query = "SELECT O_ID, O_SellPrice, O_Customer, O_Destination, T_ID FROM Outgoing NATURAL INNER JOIN Transaction where t_id=%s"
        try:
            cursor.execute(query, (oid,))
            result = cursor.fetchone()
            return result
        except Exception as e:
            print("An error occurred: ", e)
        finally:
            cursor.close()

    def insertOutgoing(self,sellprice,customer,destination,transactionID):
        cursor = self.conn.cursor()
        query = "insert into outgoing(O_SellPrice, O_Customer, O_Destination, T_ID) values (%s, %s, %s, %s) returning O_ID"
        cursor.execute(query, (sellprice,customer,destination,transactionID,))
        O_ID = cursor.fetchone()[0]
        self.conn.commit()
        return O_ID
    
    def deleteById(self, oid):
        cursor = self.conn.cursor()
        query = " delete FROM Outgoing where o_id =%s"
        cursor.execute(query, (oid,))
        count = cursor.rowcount
        self.conn.commit()
        return count
    
    def putByID(self,oid,sellprice,customer,destination,transactionID):
        cursor = self.conn.cursor()
        query = "update outgoing set O_SellPrice = %s, O_Customer = %s, O_Destination = %s, T_ID = %s where o_id = %s;"
        cursor.execute(query, (sellprice,customer,destination,transactionID, oid))
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
    
