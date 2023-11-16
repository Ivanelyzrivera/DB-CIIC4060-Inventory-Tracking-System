from config.dbconfig import pg_config
import psycopg2

class UserDAO:
    def __init__(self):
        connection_url = "host = localhost dbname =%s user=%s password=%s" % (pg_config['dbname'],
         pg_config['user'],
         pg_config['password'])
        print("Connection URL: " + connection_url)
        self.conn = psycopg2.connect(connection_url)
    
    
    def getAllUsers(self):
        cursor = self.conn.cursor()
        result = []
        query = "SELECT U_ID, U_FirstName, U_LastName, U_Email, U_Password, U_Salary, U_HireDate, U_Position, W_ID FROM Users;"
        # try:
        cursor.execute(query)
        for row in cursor:
            result.append(row)
        cursor.close()
        return result
        # except Exception as e:
        #     print("An error occurred: ", e)
        # finally:
        #     cursor.close()