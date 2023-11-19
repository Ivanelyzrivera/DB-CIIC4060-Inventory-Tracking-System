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
        query  = "SELECT S_ID,S_Name,S_Address,S_Email,S_PhoneNumber,S_City from Supplier"
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
    
    def getsupplierbyID(self,sid):
        cursor = self.conn.cursor()
        query = "SELECT S_ID,S_Name,S_Address,S_Email,S_PhoneNumber,S_City from Supplier where s_id =%s"
        try:
            cursor.execute(query, (sid,))
            result = cursor.fetchone()
            return result
        except Exception as e:
            print("An error occurred: ", e)
        finally:
            cursor.close()

    def insertSupplier(self,name,address,email,phoneNumber,city):
        cursor = self.conn.cursor()
        query = "insert into supplier(S_Name,S_Address,S_Email,S_PhoneNumber,S_City) values (%s, %s, %s, %s, %s) returning S_ID"
        cursor.execute(query, (name,address,email,phoneNumber,city,))
        S_ID = cursor.fetchone()[0]
        self.conn.commit()
        return S_ID
    
    def deleteById(self, sid):
        cursor = self.conn.cursor()
        query = " delete FROM Supplier where s_id =%s"
        cursor.execute(query, (sid,))
        count = cursor.rowcount
        self.conn.commit()
        return count

    def putById(self,sid ,name,address,email,phoneNumber,city):
        cursor = self.conn.cursor()
        query = "update supplier set S_Name = %s, S_Address =%s, S_Email = %s, S_PhoneNumber = %s ,S_City = %s where s_id = %s;"
        cursor.execute(query, (name,address,email,phoneNumber,city, sid,))
        count = cursor.rowcount
        self.conn.commit()
        return count
    
    def getTop3SuppliersPerWarehouse(self, wid):
        cursor = self.conn.cursor()
        query = """
            Select s_id, s_name, count(t_id) as transaction_count
            FROM supplier natural inner join incoming natural inner join transaction
            where w_id = %s
            group by s_id, s_name
            order by count(t_id) desc
            limit 3
        """
        try:
            cursor.execute(query, (wid,))
            result = cursor.fetchall()
            return result
        except Exception as e:
            print("An error occurred: ", e)
        finally:
            cursor.close()
    
    def validateWarehouseAssociation(self, uid, wid):
        cursor = self.conn.cursor()
        query = """
            select *
            from Users
            where U_ID = %s and W_ID = %s
        """
        cursor.execute(query, (uid, wid))
        result = cursor.fetchone()
        cursor.close()
        return result