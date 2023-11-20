from flask import jsonify
from dao.racks import RackDAO

class RackHandler:
    

    def mapToDict(self,t):
        result = {
            'R_ID': t[0],
            'R_Capacity': t[1],
            'R_Stock': t[2],
            'W_ID': t[3],
            'P_ID': t[4]
        }
        return result


    def getAllRacks(self):
        dao = RackDAO()
        try:
            dbtuples = dao.getAllRacks()
            result = []
            for e in dbtuples:
                result.append(self.mapToDict(e))
            return jsonify(result)
        except Exception as e:
            print(f"An error occurred while getting all racks: {e}")
            return jsonify({'error': 'An error occurred while retrieving racks'}), 500
   

    def getracksID(self , rid):
        dao = RackDAO()
        result = dao.getracksID(rid)
        if result:
            return jsonify(result)
        else:
            return jsonify("Not found"), 404

    def insertRacks(self,data):
        capacity = data['R_Capacity']
        stock = data['R_Stock']
        warehouseID = data['W_ID']
        partID = data['P_ID']
        if capacity and stock and warehouseID and partID:
            dao = RackDAO()
            rid = dao.insertRacks(capacity, stock, warehouseID, partID)
            data['R_ID'] = rid
            return jsonify(data),201
        else:
            return jsonify("Bad Data or Unexpected attribute values, "), 400
            

    def deleteById(self, rid):
        dao = RackDAO()
        result = dao.deleteById(rid)
        if result:
            return jsonify("Delete was Succesful"),200
        else:
            return jsonify("Not found"), 404

    def putById(self,rid,data):
        capacity = data['R_Capacity']
        stock = data['R_Stock']
        warehouseID = data['W_ID']
        partID = data['P_ID']
        if rid and capacity and stock and warehouseID and partID:
            dao = RackDAO()
            flag = dao.putById(rid,capacity, stock, warehouseID, partID)
            if flag:
                return jsonify(data),201
            else:
                return jsonify ("Not Found"),400
        else:
            return jsonify("Bad Data or Unexpected attribute values, "), 400
        
        
    def quantityOfPartsInRack(self,rid):
        dao = RackDAO()
        result = dao.quantityOfPartsInRack(rid)
        if result:
            return jsonify(result)
        else:
            return jsonify("Not found"), 404

    def get5MostExpensiveRacks(self, wid):
        dao = RackDAO()
        try:
            dbtuples = dao.get5MostExpensiveRacks(wid)
            result = []
            for e in dbtuples:
                result.append(e)
            return jsonify(result)
        except Exception as e:
            print(f"An error occurred while getting all racks: {e}")
            return jsonify({'error': 'An error occurred while retrieving racks'}), 500   
        
    def validateUserWarehouse(self, uid, wid):
        dao = RackDAO()
        warehouseAssociation = dao.validateWarehouseAssociation(uid, wid)
        return warehouseAssociation is not None