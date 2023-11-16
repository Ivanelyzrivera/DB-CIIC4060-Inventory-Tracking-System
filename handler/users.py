from flask import jsonify
from dao.users import UserDAO

class UserHandler:
    

    def mapToDict(self,t):
        result = {}
        result['U_ID'] = t[0]
        result['U_FirstName'] = t[1]
        result['U_LastName'] = t[2]
        result['U_Email'] = t[3]
        result['U_Password'] = t[4]
        result['U_Salary'] = t[5]
        result['U_HireDate'] = t[6]
        result['U_Position'] = t[7]
        result['W_ID'] = t[8]
        return result


    def getAllUsers(self):
        dao = UserDAO()
        # try:
        dbtuples = dao.getAllUsers()
        result = []
        for e in dbtuples:
            result.append(self.mapToDict(e))
        return jsonify(result)
        # except Exception as e:
        #     print(f"An error occurred while getting all users: {e}")
        #     return jsonify({'error': 'An error occurred while retrieving users'}), 500
