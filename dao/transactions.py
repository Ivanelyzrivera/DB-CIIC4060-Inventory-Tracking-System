from config.dbconfig import pg_config
import psycopg2

class TransactionDAO:
    def __init__(self):
        connection_url = "host = ec2-107-22-101-0.compute-1.amazonaws.com dbname =%s user=%s password=%s" % (pg_config['dbname'],
         pg_config['user'],
         pg_config['password'])
        print("Connection URL: " + connection_url)
        self.conn = psycopg2.connect(connection_url)


    def getAllTransactions(self):
        cursor = self.conn.cursor()
        query = "SELECT T_ID, T_Date, T_Year, T_Quantity, P_ID, W_ID, U_ID FROM Transaction"
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

    def getTransactionByID(self,tid):
        cursor = self.conn.cursor()
        query = "SELECT T_ID, T_Date, T_Year, T_Quantity, P_ID, W_ID, U_ID FROM Transaction where t_id =%s"
        try:
            cursor.execute(query, (tid,))
            result = cursor.fetchone()
            return result
        except Exception as e:
            print("An error occurred: ", e)
        finally:
            cursor.close()

    def insertTransaction(self,date,year,quantity,partsID,warehouseID,userID):
        cursor = self.conn.cursor()
        query = "insert into transaction(T_Date, T_Year, T_Quantity, P_ID, W_ID, U_ID) values (%s, %s, %s, %s,%s, %s) returning T_ID"
        cursor.execute(query, (date,year,quantity,partsID,warehouseID,userID))
        T_ID = cursor.fetchone()[0]
        self.conn.commit()
        return T_ID

    def putByID(self,tid ,date,year,quantity,partsID,warehouseID,userID):
        cursor = self.conn.cursor()
        query = "update transaction set T_Date = %s, T_Year =%s, T_Quantity =%s,  P_ID = %s, W_ID = %s ,U_ID = %s where T_ID =%s;"
        cursor.execute(query, (date,year,quantity,partsID,warehouseID,userID,tid))
        count = cursor.rowcount
        self.conn.commit()
        return count

    def top3DaysSmallestIncoming(self, wid):
        cursor = self.conn.cursor()
        query = """
            select T_Date, T_Year, sum(P_Price * T_Quantity) as TotalDailyCost
            from Transaction natural inner join Part natural inner join Incoming
            where W_ID = %s
            group by T_Date, T_Year
            order by TotalDailyCost asc
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