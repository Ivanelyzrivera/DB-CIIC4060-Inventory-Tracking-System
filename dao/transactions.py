from config.dbconfig import pg_config
import psycopg2

class TransactionDAO:
	def __init__(self):
		connection_url = "host = localhost dbname =%s user=%s password%s" %  (pg_config['dbname'],
		  pg_config['user'],
		  pg_config['password'])
		print("Connnection URL: " + connection_url)
		self.conn = psycopg2.connect(connection_url)

	def getAllTransactions(self):
		cursor = self.conn.cursor()
		result = []
		query = "Select T_ID,T_Date,T_Quantity,P_ID,W_ID,U_ID From Transaction"
		cursor.execute(query)
		for row in cursor:
			result.append(row)
		return result
