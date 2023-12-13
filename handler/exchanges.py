from flask import jsonify
from dao.exchanges import ExchangeDAO
from dao.transactions import TransactionDAO
from dao.racks import RackDAO
from dao.parts import PartDAO

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
        reason = data['E_Reason']
        warehouseIDdestination = data['W_ID_Destination']
        userIDdestination = data['U_ID_Destination']

        dao = ExchangeDAO()

        warehouseStockRes = PartDAO().getPartStockInWarehouse(warehouseID,partID)
        warehouseStock = 0
        for e in warehouseStockRes:
            warehouseStock = e[1]
            break

        if quantity > warehouseStock:
            return jsonify("Bad Data or Unexpected attribute values, "), 400
        
        transactionID = TransactionDAO().insertTransaction(date,year,quantity,partID,warehouseID,userID)
        foundRack = dao.findRackToPlace(partID, warehouseIDdestination)

        foundRackRemove = dao.findRackToPlace(partID, warehouseID)
        quantityToRemove = quantity

        if transactionID:

            for e in foundRackRemove:
                rackID = e[2]
                rackStock = e[3]
                rackCapacity = e[4]
                if quantityToRemove >= rackStock:
                    quantityToRemove -= rackStock
                    rackStock = 0
                    emptiedRack = RackDAO().putByID(rackID,rackCapacity,rackStock,warehouseID,partID)
                else:
                    rackStock -= quantityToRemove
                    quantityToRemove = 0
                    updatedRack = RackDAO().putByID(rackID,rackCapacity,rackStock,warehouseID,partID)
                
            
            rackID = -1

            for e in foundRack:
                rackID = e[2]
                rackStock = e[3]
                rackCapacity = e[4]

                if rackID == -1:                      #if no rack exists in that warehouse with that part
                    if quantity < 500:
                        rackCapacity = 1000         # Racks should be minimum 1000
                    else:
                        rackCapacity = quantity*2  # Always have space in new rack, so capacity is double transaction qty

                    rackID = RackDAO().insertRacks(rackCapacity, quantity, warehouseIDdestination, partID) # Create new rack
                    break

                else:                                           # rack with selected part exists in selected warehouse
                    
                    if quantity > (rackCapacity-rackStock):     # If transaction carries more than what fits in rack
                        if rackStock < rackCapacity:
                            quantity -= (rackCapacity-rackStock)    # take what fits in rack
                            rackStock = rackCapacity                # fill rack
                            filledRack = RackDAO().putByID(rackID,rackCapacity, rackStock, warehouseIDdestination, partID)  # Update filled rack
                        rackID = -1
                        continue
                    
                    else:                                                                               # the entirety of the transaction fits in rack
                        rackStock += quantity                                                           # add quantity to stock
                        rackID = RackDAO().putByID(rackID,rackCapacity, rackStock, warehouseIDdestination, partID)      # Update rack with transaction
                        break

            else:                               # If all racks are at capacity
                if quantity < 500:
                    rackCapacity = 1000         # Racks should be minimum 1000
                else:
                    rackCapacity = quantity*2  # Always have space in new rack, so capacity is double transaction qty

                rackID = -1
                rackID = RackDAO().insertRacks(rackCapacity, quantity, warehouseIDdestination, partID) # Create new rack

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
        

        


