from flask import jsonify
from dao.exchanges import ExchangeDAO
from dao.transactions import TransactionDAO
from dao.racks import RackDAO

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
        date = data['T_Date']
        year = data['T_Year']
        quantity = data['T_Quantity']
        partID = data['P_ID']
        warehouseID = data['W_ID']
        userID = data['U_ID']

        dao = ExchangeDAO()

        transactionID = TransactionDAO().insertTransaction(date,year,quantity,partID,warehouseID,userID)
        foundRack = dao.findRackToPlace(partID, warehouseID)

        rackID = -1

        if transactionID:
            for e in foundRack:
                rackID = e[2]
                rackStock = e[3]
                rackCapacity = e[4]
                if rackStock < rackCapacity:
                    break

            if rackID == -1:                      #if no rack exists in that warehouse with that part
                if quantity < 500:
                    rackCapacity = 1000         # Racks should be minimum 1000
                else:
                    rackCapacity = quantity*2  # Always have space in new rack, so capacity is double transaction qty

                capacity = rackCapacity
                stock = quantity
                rackID = RackDAO().insertRacks(rackCapacity, quantity, warehouseID, partID) # Create new rack

            else:                                           # rack with selected part exists in selected warehouse
                
                if quantity > (rackCapacity-rackStock):     # If transaction carries more than what fits in rack
                    quantity -= (rackCapacity-rackStock)    # take what fits in rack
                    rackStock = rackCapacity                # fill rack
                    
                    if quantity < 500:
                        rackCapacity = 1000
                    else:
                        rackCapacity = quantity*2
                    
                    filledRack = RackDAO().putByID(rackID,rackCapacity, rackStock, warehouseID, partID)  # Update filled rack
                    rackID = RackDAO().insertRacks(rackCapacity, quantity, warehouseID, partID)      # Create new rack with remainder
                
                else:                                                                               # the entirety of the transaction fits in rack
                    rackStock += quantity                                                           # add quantity to stock
                    stockedRack = RackDAO().putByID(rackID,rackCapacity, rackStock, warehouseID, partID)      # Update rack with transaction

            reason = data['E_Reason']
            warehouseIDdestination = data['W_ID_Destination']
            userIDdestination = data['U_ID_Destination']
            if reason and warehouseIDdestination and userIDdestination and transactionID:
                eid = dao.insertExchange(reason,warehouseIDdestination,userIDdestination,transactionID)
                data['E_ID'] = eid
                data['T_ID'] = transactionID
                return jsonify(data),201
            else:
                return jsonify("Bad Data or Unexpected attribute values, "), 400
        else:
            return jsonify("Bad Data or Unexpected attribute values, "), 400
        
    def deleteById(self, eid):
        dao = ExchangeDAO()
        result = dao.deleteById(eid)
        if result :
            return jsonify("Delete was Succesful"),200
        else:
            return jsonify("Not found"), 404
    
    def putByID(self,eid ,data):
        reason = data['E_Reason']
        warehouseIDdestination = data['W_ID_Destination']
        userIDdestination = data['U_ID_Destination']
        transactionID = data['T_ID']
        if eid and reason and warehouseIDdestination and userIDdestination and transactionID:
            dao = ExchangeDAO()
            flag = dao.putByID(eid,reason,warehouseIDdestination,userIDdestination,transactionID)
            if flag:
                return jsonify(data),201
            else:
                return jsonify ("Not Found"),400
        else:
            return jsonify("Bad Data or Unexpected attribute values, "), 400
        

        


