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
        query  = "Select W_ID,W_Name,W_Address,W_City From Warehouse"
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
            
    def getwarehousebyID(self,wid):
        cursor = self.conn.cursor()
        query = "SELECT W_ID,W_Name,W_Address,W_City From Warehouse where w_id =%s"
        try:
            cursor.execute(query, (wid,))
            result = cursor.fetchone()
            return result
        except Exception as e:
            print("An error occurred: ", e)
        finally:
            cursor.close()


    def insertWarehouse(self,name,address,city, price):
        cursor = self.conn.cursor()
        query = "insert into warehouse(W_Name,W_Address,W_City)) values (%s, %s, %s, %s) returning W_ID"
        cursor.execute(query, (name, address, city,))
        W_ID = cursor.fetchone()[0]
        self.conn.commit()
        return W_ID
    
    def deleteById(self, wid):
        cursor = self.conn.cursor()
        query = " delete FROM Warehouse where w_id =%s"
        cursor.execute(query, (wid,))
        count = cursor.rowcount
        self.conn.commit()
        return count
        
    def putById(self,wid,name,address,city, price):
        cursor = self.conn.cursor()
        query = "update warehouse set W_Name = %s, W_Address =%s, W_City =%s where w_id = %s;"
        cursor.execute(query, (name, address, city, wid,))
        count = cursor.rowcount
        self.conn.commit()
        return count
    
    def getTop10WarehousesMostRacks(self):
        cursor = self.conn.cursor()
        query = """
            SELECT W_ID,W_Name,W_Address,W_City, count(r_id) as Rack_Count
            FROM warehouse NATURAL INNER JOIN rack
            GROUP BY W_ID,W_Name,W_Address,W_City
            ORDER BY count(r_id) desc
            LIMIT 10
        """
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Exception as e:
            print("An error occurred: ", e)
        finally:
            cursor.close()
    
    def getTop5WarehousesMostIncomings(self):
        cursor = self.conn.cursor()
        query = """
            SELECT W_ID,W_Name,W_Address,W_City, count(I_ID) as incoming_count
            FROM warehouse NATURAL INNER JOIN transaction NATURAL INNER JOIN incoming
            GROUP BY W_ID,W_Name,W_Address,W_City
            ORDER BY count(I_ID) desc
            LIMIT 5
        """
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Exception as e:
            print("An error occurred: ", e)
        finally:
            cursor.close()
            
    def getTop5WarehousesThatDeliverMostExchanges(self): # Top 5 warehouse that delivers the most exchanges
        cursor = self.conn.cursor()
        query = """
            SELECT W_ID, W_Name, W_Address, W_City, COUNT(T_ID) AS MostExchanges
            FROM warehouse NATURAL INNER JOIN transaction 
            GROUP BY W_ID,W_Name,W_Address,W_City
            ORDER BY MostExchanges DESC
            LIMIT 5
        """
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Exception as e:
            print("An error occurred: ", e)
        finally:
            cursor.close()

    def getTop3WarehouseCitiesMostTransactions(self):
        cursor = self.conn.cursor()
        query = """
            select w_city, count(t_id) as transaction_count
            FROM warehouse natural inner join transaction
            group by w_city
            order by count(t_id) desc
            limit 3
        """
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Exception as e:
            print("An error occurred: ", e)
        finally:
            cursor.close()
    
    def getTop3WarehousesLeastOutgoings(self):
        cursor = self.conn.cursor()
        query = """
            select W_ID, count(o_id) as outgoing_transaction_count
            from transaction natural inner join outgoing
            group by W_ID
            order by count(o_id)
            limit 3
        """
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Exception as e:
            print("An error ocurred: ", e)
        finally:
            cursor.close()