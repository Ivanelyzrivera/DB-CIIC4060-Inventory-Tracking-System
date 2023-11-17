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
    
    def deleteById(self, pid):
        cursor = self.conn.cursor()
        query = " delete FROM Part where p_id =%s"
        cursor.execute(query, (pid,))
        count = cursor.rowcount
        self.conn.commit()
        return count
        
    def putById(self,pid ,type,color,weight,name,price,manufacturer,supplierID):
        cursor = self.conn.cursor()
        query = "update part set P_Type = %s, P_Color =%s, P_Weight = %s, P_Name = %s ,P_Price = %s,P_Manufacturer = %s,S_ID = %s where p_id = %s;"
        cursor.execute(query, (type, color, weight, name, price, manufacturer, supplierID, pid,))
        count = cursor.rowcount
        self.conn.commit()
        return count
    
    def getpricebyID(self, pid):
        cursor = self.conn.cursor()
        query = "SELECT P_Price FROM Part where p_id =%s"
        try:
            cursor.execute(query, (pid,))
            result = cursor.fetchone()
            return result
        except Exception as e:
            print("An error occurred: ", e)
        finally:
            cursor.close()

    def getAllPriceOfParts(self):
        cursor = self.conn.cursor()
        query = "SELECT P_Price FROM Part"
        try:
            cursor.execute(query)
            result = [row[0] for row in cursor.fetchall()]  # Extract the first column value (P_Price)
            return result
        except Exception as e:
            print("An error occurred: ", e)
        finally:
            cursor.close()


    def partsSuppliedBySupplier(self, sid):
        cursor = self.conn.cursor()
        query = """
        SELECT *
        FROM part
        JOIN supplier ON part.s_id = supplier.s_id
        WHERE supplier.s_id = %s;
        """
        try:
            cursor.execute(query, (sid,))
            result = cursor.fetchall()
            return result
        except Exception as e:
            print("An error occurred: ", e)
        finally:
            cursor.close()

    def partsInRack(self, rack_id):
        cursor = self.conn.cursor()
        query = """
            SELECT Part.*
            FROM Part
            NATURAL INNER JOIN Rack
            WHERE Rack.R_ID = %s;
        """
        try:
            cursor.execute(query, (rack_id,))
            parts_in_rack = cursor.fetchall()
            return parts_in_rack
        except Exception as e:
            print("An error occurred: ", e)
        finally:
            cursor.close()





