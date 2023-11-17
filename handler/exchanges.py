from flask import jsonify
from dao.exchanges import ExchangeDAO

class ExchangeHandler:
    

    def mapToDict(self,t):
        result = {
            'E_ID': t[0],
            'E_Reason': t[1],
            'W_ID_Destination': t[2],
            'U_ID_Destination': t[3],
            'T_ID': t[4]
        }
        return result


    def getAllExchanges(self):
        dao = ExchangeDAO()
        try:
            dbtuples = dao.getAllExchanges()
            result = []
            for e in dbtuples:
                result.append(self.mapToDict(e))
            return jsonify(result)
        except Exception as e:
            print(f"An error occurred while getting all exchanges: {e}")
            return jsonify({'error': 'An error occurred while retrieving exchanges'}), 500
        
    def getexchangebyID(self , eid):
        dao = ExchangeDAO()
        result = dao.getexchangebyID(eid)
        if result :
            return jsonify(self.mapToDict(result))
        else:
            return jsonify("Not found"), 404
        
    def insertExchange(self,data):
        reason = data['E_Reason']
        warehouseIDdestination = data['W_ID_Destination']
        userIDdestination = data['U_ID_Destination']
        transactionID = data['T_ID']
        if reason and warehouseIDdestination and userIDdestination and transactionID:
            dao = ExchangeDAO()
            eid = dao.insertExchange(reason,warehouseIDdestination,userIDdestination,transactionID)
            data['E_ID'] = eid
            return jsonify(data),201
        else:
            return jsonify("Bad Data or Unexpected attribute values, "), 400
        
    def deleteById(self, eid):
        dao = ExchangeDAO()
        result = dao.deleteById(eid)
        if result :
            return jsonify("Delete was Succesful"),200
        else:
            return jsonify("Not found"), 404
    
    def putById(self,eid ,data):
        reason = data['E_Reason']
        warehouseIDdestination = data['W_ID_Destination']
        userIDdestination = data['U_ID_Destination']
        transactionID = data['T_ID']
        if eid and reason and warehouseIDdestination and userIDdestination and transactionID:
            dao = ExchangeDAO()
            flag = dao.putById(eid,reason,warehouseIDdestination,userIDdestination,transactionID)
            if flag:
                return jsonify(data),201
            else:
                return jsonify ("Not Found"),400
        else:
            return jsonify("Bad Data or Unexpected attribute values, "), 400
        

        


