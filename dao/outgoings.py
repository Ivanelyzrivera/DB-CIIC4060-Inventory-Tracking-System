from config.dbconfig import pg_config
import psycopg2

class OutgoingDAO:
	def __init__(self):
		connection_url = "host = localhost dbname =%s user=%s password=%s" %  (pg_config['dbname'],
		  pg_config['user'],
		  pg_config['password'])
		print("Connnection URL: " + connection_url)
		self.conn = psycopg2.connect(connection_url)


	def getAllOutgoings(self):
		cursor = self.conn.cursor()
		query = "Select O_ID,O_SellPrice,O_Customer,O_Destination,T_ID from Outgoing"
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