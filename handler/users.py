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
        try:
            dbtuples = dao.getAllUsers()
            result = []
            for e in dbtuples:
                result.append(self.mapToDict(e))
            return jsonify(result)
        except Exception as e:
            print(f"An error occurred while getting all users: {e}")
            return jsonify({'error': 'An error occurred while retrieving users'}), 500
    
    def getuserbyID(self , uid):
        dao = UserDAO()
        result = dao.getuserbyID(uid)
        if result :
            return jsonify(self.mapToDict(result))
        else:
            return jsonify("Not found"), 404

    def insertUser(self,data):
        firstName = data['U_FirstName']
        lastName = data['U_LastName']
        email = data['U_Email']
        password = data['U_Password']
        salary = data['U_Salary']
        hireDate = data['U_HireDate']
        position = data['U_Position']
        warehouseID = data['W_ID']
        if firstName and lastName and email and password and salary and hireDate and position and warehouseID:
            dao = UserDAO()
            uid = dao.insertUser(firstName,lastName,email,password,salary,hireDate,position,warehouseID)
            data['U_ID'] = uid
            return jsonify(data),201
        else:
            return jsonify("Bad Data or Unexpected attribute values, "), 400
        
    def deleteById(self, uid):
        dao = UserDAO()
        result = dao.deleteById(uid)
        if result :
            return jsonify("Delete was Succesful"),200
        else:
            return jsonify("Not found"), 404

    def putByID(self,uid ,data):
        firstName = data['U_FirstName']
        lastName = data['U_LastName']
        email = data['U_Email']
        password = data['U_Password']
        salary = data['U_Salary']
        hireDate = data['U_HireDate']
        position = data['U_Position']
        warehouseID = data['W_ID']
        if uid and firstName and lastName and email and password and salary and hireDate and position and warehouseID:
            dao = UserDAO()
            flag = dao.putByID(uid,firstName,lastName,email,password,salary,hireDate,position,warehouseID)
            if flag:
                return jsonify(data),201
            else:
                return jsonify ("Not Found"),400
        else:
            return jsonify("Bad Data or Unexpected attribute values, "), 400
        
    def getTop3UsersMostTransactions(self):
        dao = UserDAO()
        try:
            dbtuples = dao.getTop3UsersMostTransactions()
            result =[]
            for e in dbtuples:
                result.append(e)
            return jsonify(result)
        except Exception as e:
            print(f"An error occurred while getting all users: {e}")
            return jsonify({'error': 'An error occurred while retrieving users'}), 500

    def get3UsersMostExchanges(self, wid):
        dao = UserDAO()
        try:
            dbtuples = dao.get3UsersMostExchanges(wid)
            result = []
            for e in dbtuples:
                result.append(e)
            return jsonify(result)
        except Exception as e:
            print(f"An error occurred while getting all users: {e}")
            return jsonify ({'error': 'An error occurred while retrieving racks'}), 500
        
    def validateUserWarehouse(self, uid, wid):
        dao = UserDAO()
        warehouseAssociation = dao.validateWarehouseAssociation(uid, wid)
        return warehouseAssociation is not None
    
    def getUserID(self,data):
        uid = data['user_id']
        return uid