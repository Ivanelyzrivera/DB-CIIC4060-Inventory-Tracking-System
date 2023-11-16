from flask import jsonify
from dao.users import UserDAO

class UserHandler:
    

    def mapToDict(self,t):
        result = {
            'U_ID': t[0],
            'U_FirstName': t[1],
            'U_LastName': t[2],
            'U_Email': t[3],
            'U_Password': t[4],
            'U_Salary': t[5],
            'U_HireDate': t[6],
            'U_Position': t[7],
            'W_ID': t[8]
        }
        return result


    def getAllUsers(self):
        dao = UsersDAO()
        try:
            dbtuples = dao.getAllUsers()
            result = []
            for e in dbtuples:
                result.append(self.mapToDict(e))
            return jsonify(result)
        except Exception as e:
            print(f"An error occurred while getting all users: {e}")
            return jsonify({'error': 'An error occurred while retrieving users'}), 500
