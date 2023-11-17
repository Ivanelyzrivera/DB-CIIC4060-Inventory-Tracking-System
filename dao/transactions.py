from config.dbconfig import pg_config
import psycopg2

class TransactionDAO:
	def __init__(self):
		connection_url = "host = localhost dbname =%s user=%s password=%s" %  (pg_config['dbname'],
		  pg_config['user'],
		  pg_config['password'])
		print("Connnection URL: " + connection_url)
		self.conn = psycopg2.connect(connection_url)

def getAllTransactions(self):
    cursor = self.conn.cursor()
    query = "SELECT T_ID, T_Date, T_Quantity, P_ID, W_ID, U_ID FROM Transaction"
    try:
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
    except Exception as e:
        print("An error occurred: ", e)
    finally:
        cursor.close()

def getTransactionByID(self,tid):
    cursor = self.conn.cursor()
    query = "SELECT T_ID, T_Date, T_Quantity, P_ID, W_ID, U_ID FROM Transaction where t_id =%s"
    try:
        cursor.execute(query, (tid,))
        result = cursor.fetchone()
        return result
    except Exception as e:
        print("An error occurred: ", e)
    finally:
        cursor.close()

def insertUser(self,date,quantity,partsID,warehouseID,userID):
    cursor = self.conn.cursor()
    query = "insert into transactions(T_Date, T_Quantity, P_ID, W_ID, U_ID) values (%s, %s, %s, %s, %s) returning T_ID"
    cursor.execute(query, (date,quantity,partsID,warehouseID,userID))
    T_ID = cursor.fetchone()[0]
    self.conn.commit()
    return T_ID

def putById(self,tid ,date,quantity,partsID,warehouseID,userID):
    cursor = self.conn.cursor()
    query = "update transactions set T_Date = %s, T_Quantity =%s, P_ID = %s, W_ID = %s ,U_ID = %s;"
    cursor.execute(query, (date,quantity,partsID,warehouseID,userID,tid))
    count = cursor.rowcount
    self.conn.commit()
    return count