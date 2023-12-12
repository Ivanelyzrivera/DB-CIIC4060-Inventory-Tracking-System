from flask import jsonify
from dao.incomings import IncomingDAO
from dao.transactions import TransactionDAO

class IncomingHandler:
    

    def mapToDict(self,t):
        result = {
            'I_ID': t[0],
            'R_ID': t[1],
            'T_ID': t[2]
        }
        return result


    def getAllIncomings(self):
        dao = IncomingDAO()
        try:
            dbtuples = dao.getAllIncomings()
            result = []
            for e in dbtuples:
                result.append(self.mapToDict(e))
            return jsonify(result)
        except Exception as e:
            print(f"An error occurred while getting all incomings: {e}")
            return jsonify({'error': 'An error occurred while retrieving incomings'}), 500
    
    def getincomingbyID(self , iid):
        dao = IncomingDAO()
        result = dao.getincomingbyID(iid)
        if result :
            return jsonify(self.mapToDict(result))
        else:
            return jsonify("Not found"), 404
    
    def insertIncoming(self,data):
        date = data['T_Date']
        year = data['T_Year']
        quantity = data['T_Quantity']
        partsID = data['P_ID']
        warehouseID = data['W_ID']
        userID = data['U_ID']

        transactionID = TransactionDAO().insertTransaction(date,year,quantity,partsID,warehouseID,userID)
        rackID = data['R_ID']
        if rackID and transactionID:
            dao = IncomingDAO()
            iid = dao.insertIncoming(rackID,transactionID)
            data['I_ID'] = iid
            data['T_ID'] = transactionID
            return jsonify(data),201
        else:
            return jsonify("Bad Data or Unexpected attribute values, "), 400
        
    def deleteById(self, iid):
        dao = IncomingDAO()
        result = dao.deleteById(iid)
        if result :
            return jsonify("Delete was Succesful"),200
        else:
            return jsonify("Not found"), 404

    def putByID(self,iid ,data):
        rackID = data['R_ID']
        transactionID = data['T_ID']
        if iid and rackID and transactionID:
            dao = IncomingDAO()
            flag = dao.putByID(iid,rackID,transactionID)
            if flag:
                return jsonify(data),201
            else:
                return jsonify ("Not Found"),400
        else:
            return jsonify("Bad Data or Unexpected attribute values, "), 400
