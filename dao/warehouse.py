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
    

    # SELECT W_ID,W_Name,W_Address,W_City, count(r_id) as Rack_Count FROM warehouse NATURAL INNER JOIN rack GROUP BY W_ID,W_Name,W_Address,W_City ORDER BY count(r_id) desc LIMIT 10;

    def partTypeByWarehouse(self):
        cursor = self.conn.cursor()
        query  = """
        SELECT w_id, p_type , sum(r_stock)
        From warehouse natural inner join rack natural inner join part
        Group By w_id,p_type
        """
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

    def warehouseRackLowStock(self, wid):
        cursor = self.conn.cursor()
        query  = """
        SELECT rack.*
        FROM rack 
        WHERE R_Stock < 0.25 * R_Capacity and W_ID = %s
        ORDER BY R_Capacity * 1.0 / R_Stock
        LIMIT 5;
        """
        try:
            cursor.execute(query,(wid,))
            result = []
            for row in cursor:
                result.append(row)
            cursor.close()
            return result
        except Exception as e:
            print("An error occurred: ", e)
        finally:
            cursor.close()

