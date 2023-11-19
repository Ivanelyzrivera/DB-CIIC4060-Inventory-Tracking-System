from config.dbconfig import pg_config
import psycopg2

class UserDAO:
    def __init__(self):
        connection_url = "host = ec2-3-210-173-88.compute-1.amazonaws.com dbname =%s user=%s password=%s" % (pg_config['dbname'],
         pg_config['user'],
         pg_config['password'])
        print("Connection URL: " + connection_url)
        self.conn = psycopg2.connect(connection_url)
    
    
    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "SELECT U_ID, U_FirstName, U_LastName, U_Email, U_Password, U_Salary, U_HireDate, U_Position, W_ID FROM Users;"
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

    def getuserbyID(self,uid):
        cursor = self.conn.cursor()
        query = "SELECT U_ID, U_FirstName, U_LastName, U_Email, U_Password, U_Salary, U_HireDate, U_Position, W_ID FROM Users where u_id =%s"
        try:
            cursor.execute(query, (uid,))
            result = cursor.fetchone()
            return result
        except Exception as e:
            print("An error occurred: ", e)
        finally:
            cursor.close()
    
    def insertUser(self,firstName,lastName,email,password,salary,hireDate,position,warehouseID):
        cursor = self.conn.cursor()
        query = "insert into users(U_FirstName, U_LastName, U_Email, U_Password, U_Salary, U_HireDate, U_Position, W_ID) values (%s, %s, %s, %s, %s, %s, %s, %s) returning U_ID"
        cursor.execute(query, (firstName,lastName,email,password,salary,hireDate,position,warehouseID,))
        U_ID = cursor.fetchone()[0]
        self.conn.commit()
        return U_ID
    
    def deleteById(self, uid):
        cursor = self.conn.cursor()
        query = " delete FROM Users where u_id =%s"
        cursor.execute(query, (uid,))
        count = cursor.rowcount
        self.conn.commit()
        return count
    
    def putById(self,uid ,firstName,lastName,email,password,salary,hireDate,position,warehouseID):
        cursor = self.conn.cursor()
        query = "update users set U_FirstName = %s, U_LastName =%s, U_Email = %s, U_Password = %s ,U_Salary = %s,U_HireDate = %s,U_Position = %s,W_ID = %s where u_id = %s;"
        cursor.execute(query, (firstName,lastName,email,password,salary,hireDate,position,warehouseID, uid,))
        count = cursor.rowcount
        self.conn.commit()
        return count

    def getTop3UsersMostTransactions(self):
        cursor = self.conn.cursor()
        query = """
            select U_ID, count(t_id) as transaction_count
            from transaction
            group by U_ID
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

    def get3UsersMostExchanges(self, wid):
        cursor = self.conn.cursor()
        query = """
            select U_ID_Destination as U_ID, count(*) AS exchange_count
            from Exchange
            where W_ID_Destination = %s
            group by U_ID_Destination
            order by exchange_count DESC
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