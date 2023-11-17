from flask import jsonify
from dao.warehouse import WarehouseDAO

class WarehouseHandler:
    
    def mapToDict(self,t):
        result = {}
        result['W_ID'] = t[0]
        result['W_Name'] = t[1]
        result['W_Address'] = t[2]
        result['W_City'] = t[3]
        return result


    def getAllWarehouses(self):
        dao = WarehouseDAO()
        try:
            dbtuples = dao.getAllWarehouses()
            result =[]
            for e in dbtuples:
                result.append(self.mapToDict(e))
            return jsonify(result)
        except Exception as e:
            print(f"An error occurred while getting all warehouses: {e}")
            return jsonify({'error': 'An error occurred while retrieving warehouses'}), 500


    def getwarehousebyID(self , wid):
        dao = WarehouseDAO()
        result = dao.getwarehousebyID(wid)
        if result :
            return jsonify(self.mapToDict(result))
        else:
            return jsonify("Not found"), 404
        
    
    def insertWarehouse(self,data):
        name = data['W_Name']
        address = data['W_Address']
        city = data['W_City']
        if  name and address and city:
            dao = WarehouseDAO()
            wid = dao.insertWarehouse(name,address,city)
            data['W_ID'] = wid
            return jsonify(data),201
        else:
            return jsonify("Bad Data or Unexpected attribute values, "), 400
        

    def deleteById(self, wid):
        dao = WarehouseDAO()
        result = dao.deleteById(wid)
        if result :
            return jsonify("Delete was Succesful"),200
        else:
            return jsonify("Not found"), 404

    def putById(self,wid ,data):
        name = data['W_Name']
        address = data['W_Address']
        city = data['W_City']
        if wid and name and address and city:
            dao = WarehouseDAO()
            flag = dao.putById(wid, name,address,city)
            if flag:
                return jsonify(data),201
            else:
                return jsonify ("Not Found"),400
        else:
            return jsonify("Bad Data or Unexpected attribute values, "), 400
        
