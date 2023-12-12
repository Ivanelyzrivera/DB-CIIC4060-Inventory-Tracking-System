from flask import jsonify
from dao.incomings import IncomingDAO
from dao.transactions import TransactionDAO
from dao.racks import RackDAO

class IncomingHandler:
    

    def mapToDict(self,t):
        result = {
            'I_ID': t[0],
            'T_ID': t[1]
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
        partID = data['P_ID']
        warehouseID = data['W_ID']
        userID = data['U_ID']

        dao = IncomingDAO()

        transactionID = TransactionDAO().insertTransaction(date,year,quantity,partID,warehouseID,userID)
        foundRack = dao.findRackToPlace(partID,warehouseID)

        rackID = -1

        if transactionID:
            for e in foundRack:
                rackID = e[2]
                rackStock = e[3]
                rackCapacity = e[4]

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

        
            
            iid = dao.insertIncoming(transactionID)
            data['I_ID'] = iid
            data['R_ID'] = rackID
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
        transactionID = data['T_ID']
        if iid and transactionID:
            dao = IncomingDAO()
            flag = dao.putByID(iid,transactionID)
            if flag:
                return jsonify(data),201
            else:
                return jsonify ("Not Found"),400
        else:
            return jsonify("Bad Data or Unexpected attribute values, "), 400
