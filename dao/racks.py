from config.dbconfig import pg_config
import psycopg2

class RackDAO:
    def __init__(self):
        connection_url = "host = localhost dbname =%s user=%s password=%s" % (pg_config['dbname'],
         pg_config['user'],
         pg_config['password'])
        print("Connection URL: " + connection_url)
        self.conn = psycopg2.connect(connection_url)
    
    
    def getAllRacks(self):
        cursor = self.conn.cursor()
        query = "SELECT R_ID, R_Capacity, R_Stock, W_ID, P_ID FROM Rack;"
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
            
    def getracksID(self,rid):
        cursor = self.conn.cursor()
        query = "SELECT R_ID, R_Capacity R_Stock, W_ID, P_ID FROM Rack where r_id =%s"
        try:
            cursor.execute(query, (rid,))
            result = cursor.fetchone()
            return result
        except Exception as e:
            print("An error occurred: ", e)
        finally:
            cursor.close()


    def insertRacks(self,capacity, stock, warehouseID, partID):
        cursor = self.conn.cursor()
        query = "insert into racks(R_Capacity R_Stock, W_ID, P_ID) values (%s, %s, %s, %s) returning R_ID"
        cursor.execute(query, (capacity, stock, warehouseID, partID,))
        P_ID = cursor.fetchone()[0]
        self.conn.commit()
        return P_ID
    
    def deleteById(self, rid):
        cursor = self.conn.cursor()
        query = " delete FROM Part where p_id =%s"
        cursor.execute(query, (rid,))
        count = cursor.rowcount
        self.conn.commit()
        return count
        
    def putById(self,rid ,capacity, stock, warehouseID, partID):
        cursor = self.conn.cursor()
        query = "update racks set R_Capacity = %s, R_Stock = %s, W_ID = %s, P_ID = %s where r_id = %s;"
        cursor.execute(query, (capacity, stock, warehouseID, partID, rid,))
        count = cursor.rowcount
        self.conn.commit()
        return count
    
    def quantityOfPartsInRack(self,rid):
        cursor = self.conn.cursor()
        query = "Select R_Stock FROM Rack where r_id =%s"
        try:
            cursor.execute(query, (rid,))
            result = cursor.fetchone()
            return result
        except Exception as e:
            print("An error occurred: ", e)
        finally:
            cursor.close()

    def get5MostExpensiveRacks(self, wid):
        cursor = self.conn.cursor()
        query = """
            select rack.R_ID, sum(part.P_Price * rack.R_Stock) as total_value
            from rack natural inner join part
            where w_id = %s 
            group by rack.R_ID
            order by sum(part.P_Price * rack.R_Stock) desc
            limit 5
        """
        try:
            cursor.execute(query, (wid,))
            result = cursor.fetchall()
            return result
        except Exception as e:
            print("An error occurred: ", e)
        finally:
            cursor.close()
            
         